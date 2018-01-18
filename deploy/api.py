#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/18 11:07 AM
# @Author  : Miracle Young
# @File    : api.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.conf import settings
from django.utils import timezone
from .models import SaltMinion
from .saltapi import SaltAPI
from asset.models import Server

SALT_API_URL = settings.SALT_API_URL
SALT_API_USERNAME = settings.SALT_API_USERNAME
SALT_API_PASSWORD = settings.SALT_API_PASSWORD


class MinionRefreshApi(APIView):
    def get(self, request, **kwargs):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _minions = saltapi.list_all_key()[0]
        _minions_pre = saltapi.list_all_key()[1]

        for _minion in _minions:
            if not SaltMinion.objects.filter(hostname=_minion):
                SaltMinion.objects.create(hostname=_minion, status=1, is_alive=False)
                ret = list(saltapi.remote_noarg_execution(_minion, 'grains.items'))[0]
                cpu = int(ret['num_cpus']) * int(ret['num_cpus'])
                cpu_arch = ret['cpuarch']
                memory = round(int(ret['mem_total']) / 1024)
                os = ret['os'] + ret['osrelease']
                os_arch = ret['osarch']
                hostname = _minion
                public_ip = ret['ip4'][1]
                sn = ret['serialnumber']
                group_env, biz, _ = hostname.split('.')
                remark = biz
                type, env = group_env.split('-')
                if type == 'web':
                    type = 1
                elif type == 'db':
                    type = 2
                elif type == 'big':
                    type = 3
                elif type == 'mid':
                    type = 4
                elif type == 'dev':
                    type = 5
                else:
                    type = 99

                if env == 'pro':
                    env = 1
                elif env == 'gl':
                    env = 2
                elif env == 'stg':
                    env = 3
                elif env == 'dev':
                    env = 4
                elif env == 'test':
                    env = '5'

                hardware_version = ret['manufacturer']
                # TODO
                # disk,

            else:
                SaltMinion.objects.filter(hostname=_minion).update(status=1, is_alive=False)
        for _minion in _minions_pre:
            if not SaltMinion.objects.filter(hostname=_minion):
                SaltMinion.objects.create(hostname=_minion, status=2, is_alive=False)
            else:
                SaltMinion.objects.filter(hostname=_minion).update(status=2, is_alive=False)

        return Response('success', status=status.HTTP_200_OK)


class MinionCheckAliveApi(APIView):
    def get(self, request):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _ret = saltapi.salt_check_alive('*')
        for host, is_alive in _ret.items():
            SaltMinion.objects.filter(hostname=host).update(is_alive=is_alive, last_alive_time=timezone.now())
        return Response('success')


class MinionApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaltMinion

    def delete(self, request, *args, **kwargs):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        pk = kwargs.get('pk')
        try:
            _minion = SaltMinion.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _ret = saltapi.delete_key(_minion.hostname)
        if _ret:
            SaltMinion.objects.filter(hostname=_minion.hostname).update(is_alive=False, status=5)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        pk = kwargs.get('pk')
        try:
            _minion = SaltMinion.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _ret = saltapi.accept_key(_minion.hostname)
        if _ret:
            SaltMinion.objects.filter(hostname=_minion.hostname).update(is_alive=False, status=1)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
