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

SALT_API_URL = settings.SALT_API_URL
SALT_API_USERNAME = settings.SALT_API_USERNAME
SALT_API_PASSWORD = settings.SALT_API_PASSWORD


class MinionImportApi(APIView):
    def get(self, request, format=None):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _minions_pre = saltapi.list_all_key()[1]
        ret = saltapi.accept_key(_minions_pre, mul=True)
        if ret:
            SaltMinion.objects.filter(hostname__in=_minions_pre).update(status=1)
            return Response(ret, status=status.HTTP_200_OK)
        else:
            return Response(ret, status=status.HTTP_400_BAD_REQUEST)

class MinionCheckAliveApi(APIView):
    def get(self, request):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _ret = saltapi.salt_check_alive('*')
        for host, is_alive in _ret.items():
            SaltMinion.objects.filter(hostname=host).update(is_alive=is_alive, last_alive_time=timezone.now())
        return Response('success')

class MinionApi(generics.RetrieveUpdateDestroyAPIView):


    def delete(self, request, *args, **kwargs):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        hostname = kwargs.get('hostname')
        _ret = saltapi.delete_key(hostname)
        if _ret:
            SaltMinion.objects.filter(hostname=hostname).update(is_alive=False)
            return super(MinionApi, self).delete(request, *args, **kwargs)
        return super(MinionApi, self).delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        hostname = kwargs.get('hostname')
        _ret = saltapi.accept_key(hostname)
        if _ret:
            _is_alive = saltapi.salt_check_alive(hostname)
            SaltMinion.objects.filter(hostname=hostname).update(is_alive=_is_alive)
            return super(MinionApi, self).delete(request, *args, **kwargs)
        return super(MinionApi, self).delete(request, *args, **kwargs)