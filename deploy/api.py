#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/18 11:07 AM
# @Author  : Miracle Young
# @File    : api.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import json, os, shutil, uuid
from common.str_parse import text2html
from .models import *
from .saltapi import SaltAPI
from asset.models import Server
from user.authentication import get_user

SALT_API_URL = settings.SALT_API_URL
SALT_API_USERNAME = settings.SALT_API_USERNAME
SALT_API_PASSWORD = settings.SALT_API_PASSWORD


def init_server(saltapi, hostname):
    _payload = saltapi.remote_one_server(hostname, 'grains.items')
    _disk = saltapi.remote_one_server(hostname, 'status.diskusage')
    _server_info = {}
    _server_info['disk'] = json.dumps(_disk)
    _server_info['cpu'] = int(_payload['num_cpus']) * int(_payload['num_cpus'])
    _server_info['memory'] = round(int(_payload['mem_total']) / 1024)
    _server_info['os'] = _payload['os'] + _payload['osrelease']
    _server_info['os_arch'] = _payload['osarch']
    _server_info['hostname'] = hostname
    _server_info['public_ip'] = _payload['ipv4'][1]
    _server_info['sn'] = _payload['serialnumber']
    try:
        type_env, biz, _ = hostname.split('.')
        type, env = type_env.split('-')
        if type == 'web':
            _server_info['type'] = 1
        elif type == 'db':
            _server_info['type'] = 2
        elif type == 'big':
            _server_info['type'] = 3
        elif type == 'mid':
            _server_info['type'] = 4
        elif type == 'dev':
            _server_info['type'] = 5
        else:
            _server_info['type'] = 99

        if env == 'pro':
            _server_info['env'] = 1
        elif env == 'gl':
            _server_info['env'] = 2
        elif env == 'stg':
            _server_info['env'] = 3
        elif env == 'dev':
            _server_info['env'] = 4
        elif env == 'test':
            _server_info['env'] = 5
    except:
        biz, _ = hostname.split('.')
        _server_info['type'] = 99
        _server_info['env'] = 99

    _server_info['remark'] = biz
    _server_info['hardware_version'] = _payload['manufacturer']
    _server_info['uuid'] = _payload['uuid']
    _server = Server(**_server_info)
    _server.save()
    return _server


def sym_link_roster(pk):
    try:
        _roster = Roster.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Response('roster does not exist', status=status.HTTP_400_BAD_REQUEST)
    # create symbol link from roster to /etc/salt/roster
    _filepath = _roster.file.path
    _rosterpath = '/etc/salt/roster'
    if os.path.exists(_rosterpath):
        os.remove(_rosterpath)
    os.symlink(_filepath, _rosterpath)


def sym_link_sls(pk):
    try:
        _sls = Sls.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Response('sls does not exist', status=status.HTTP_400_BAD_REQUEST)
    # create symbol link from /media/sls/name/sls, /media/sls/name/top.sls to /etc/salt/sls/, /etc/salt/top.sls
    # _filepath = sls/biz_username_ts
    _filepath = _sls.file.path + '.dir'
    _slsdir_srcpath = os.path.join(_filepath, 'sls')
    _slsdir_dstpath = '/etc/salt/sls'
    _topsls_srcpath = os.path.join(_filepath, 'top.sls')
    _topsls_dstpath = '/etc/salt/top.sls'
    # remove /etc/salt/sls, /etc/salt/top.sls
    try:
        os.remove(_slsdir_dstpath)
        os.remove(_topsls_dstpath)
    except:
        pass
    try:
        os.symlink(_slsdir_srcpath, _slsdir_dstpath)
        os.symlink(_topsls_srcpath, _topsls_dstpath)
    except:
        return False
    return True


def from_dir_get_files(path: str):
    if os.path.isdir(path):
        for item in os.walk(path):
            if item[2]:
                for file in item[2]:
                    _filepath = os.path.join(item[0], file)
                    with open(_filepath) as f:
                        yield _filepath, f.read()
    else:
        with open(path) as f:
            yield path, f.read()


# get directory tree
def get_tree(path='.', depth=0):
    _tree = ''

    def inner(path, depth):
        nonlocal _tree
        if depth == 0:
            _tree += 'root:[' + path + ']'

        for item in os.listdir(path):
            if item not in ('.git', '.idea', 'migrations', '__pycache__'):
                _line = "|\t" * depth + "|--" + item + '\n'
                print(_line)
                _tree += _line
                _newitem = path + '/' + item
                if os.path.isdir(_newitem):
                    inner(_newitem, depth + 1)
        return _tree

    return inner(path, depth)


class MinionRefreshApi(APIView):
    def get(self, request, **kwargs):
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _minions = _saltapi.list_all_key()[0]
        _minions_pre = _saltapi.list_all_key()[1]
        for _minion in _minions:
            if not SaltMinion.objects.filter(hostname=_minion):
                _salt_minion = SaltMinion(hostname=_minion, status=1, is_alive=False)
                # retrieve server info and initial it
                _salt_minion.server = init_server(_saltapi, _minion)
                _salt_minion.save()
        for _minion in _minions_pre:
            if not SaltMinion.objects.filter(hostname=_minion):
                SaltMinion.objects.create(hostname=_minion, status=2, is_alive=False)
            else:
                SaltMinion.objects.filter(hostname=_minion).update(status=2, is_alive=False)

        return Response('success', status=status.HTTP_200_OK)


class MinionCheckAliveApi(APIView):
    def get(self, request):
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _ret = _saltapi.salt_check_alive('*')
        for host, is_alive in _ret.items():
            SaltMinion.objects.filter(hostname=host).update(is_alive=is_alive, last_alive_time=timezone.now(),
                                                            update_time=timezone.now())
        return Response('success')


class MinionApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaltMinion

    def delete(self, request, *args, **kwargs):
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        pk = kwargs.get('pk')
        try:
            _minion = SaltMinion.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _ret = _saltapi.delete_key(_minion.hostname)
        if _ret:
            SaltMinion.objects.filter(hostname=_minion.hostname).update(is_alive=False, status=5)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        pk = kwargs.get('pk')
        try:
            _minion = SaltMinion.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _ret = _saltapi.accept_key(_minion.hostname)
        if _ret:
            _minion.status = 1
            _minion.server = init_server(_saltapi, _minion.hostname)
            _minion.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MinionCmdApi(APIView):
    def post(self, request, *args, **kwargs):
        _type = request.data.get('type', '')
        if _type == 'glob':
            _server = request.data.get('servers', '')
        elif _type == 'list':
            _server = request.data.getlist('servers[]', '')
        _cmds = request.data.getlist('cmds[]', '')
        _raw_args = request.data.getlist('args[]', [])
        _args = [_arg.split(',') for _arg in _raw_args]
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _payload = _saltapi.remote_execution(_server, _cmds, tgt_type=_type, arg=_args)
        return Response(_payload, status=status.HTTP_200_OK)


class RosterApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roster.objects.all()

    def get(self, request, *args, **kwargs):
        _pk = kwargs.get('pk', -1)
        try:
            _roster = Roster.objects.get(pk=_pk)
        except ObjectDoesNotExist:
            raise Response('roster does not exist', status=status.HTTP_404_NOT_FOUND)
        with open(_roster.file.path, 'r') as f:
            _content = f.read()
        return Response(text2html(_content), status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        _pk = kwargs.get('pk', -1)
        try:
            _roster = Roster.objects.get(pk=_pk)
        except ObjectDoesNotExist:
            raise Response('roster does not exist', status=status.HTTP_404_NOT_FOUND)
        _roster.status = 2
        _roster.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InstallMinionApi(APIView):
    def get(self, request, *args, **kwargs):
        _pk = self.kwargs.get('roster_id', -1)
        sym_link_roster(_pk)
        # cp install_salt.sh from master to minion
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _cp_fun = 'cp.get_file'
        _cp_arg = ['salt://install_salt.sh', '/etc/salt/', ]
        _cp_payload = _saltapi.ssh_execution(tgt='*', fun=_cp_fun, arg=_cp_arg)
        # install salt-minion
        _sh_fun = 'cmd.run'
        _sh_arg = ['sudo sh /etc/salt/install_salt.sh', ]
        _sh_payload = _saltapi.ssh_execution(tgt='*', fun=_sh_fun, arg=_sh_arg)
        _payload = {}
        # dump payload
        for _host, _ret in _cp_payload.items():
            _payload[_host] = _sh_payload[_host] if _ret['return'] else _cp_payload[_host]
        # whatever return payload
        return Response(_payload, status=status.HTTP_200_OK)


class SSHCmdApi(APIView):
    def post(self, request, *args, **kwargs):
        _pk = request.data.get('roster_id', -1)
        sym_link_roster(_pk)
        _fun = request.data.get('cmds', '')
        _raw_args = request.data.get('args', '')
        _args = _raw_args.split(',')
        _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
        _raw_payload = _saltapi.ssh_execution(tgt='*', fun=_fun, arg=_args)
        _payload = {}
        for _host, _ret in _raw_payload.items():
            _payload[_host] = _ret if _ret.get('stderr') else text2html(_ret['return'])
        return Response(_payload, status=status.HTTP_200_OK)


class SLSApi(APIView):
    def get(self, request, *args, **kwargs):
        _pk = kwargs.get('pk', -1)
        try:
            _sls = Sls.objects.get(pk=_pk)
        except ObjectDoesNotExist:
            raise Response('sls does not exist', status=status.HTTP_400_BAD_REQUEST)
        _payload = ["<h5>{}</h5>{}".format(_filename, text2html(_content)) for _filename, _content in
                    from_dir_get_files(_sls.file.path + '.dir')]
        return Response(_payload, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        _pk = kwargs.get('pk', -1)
        try:
            _sls = Sls.objects.get(pk=_pk)
        except ObjectDoesNotExist:
            raise Response('sls does not exist', status=status.HTTP_404_NOT_FOUND)
        _sls.status = 2
        _sls.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SLSCmdApi(APIView):
    def post(self, request, *args, **kwargs):
        _tgt = request.data.get('tgt', '')
        _sls_id = request.data.get('sls_id', -1)
        # symlink /etc/salt/top.sls /etc/salt/sls/*
        if sym_link_sls(_sls_id):
            _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
            _payload = _saltapi.remote_execution(tgt=_tgt, fun='state.apply')
            return Response(_payload, status=status.HTTP_200_OK)
        else:
            raise Response('', status=status.HTTP_400_BAD_REQUEST)


class FileUploadApi(APIView):
    def post(self, request, *args, **kwargs):
        _glob = self.request.data.get('glob', '')
        _dst_dir = self.request.data.get('dst_dir', '')
        if _glob and _dst_dir:
            _saltapi = SaltAPI(url=SALT_API_URL, username=SALT_API_USERNAME, password=SALT_API_PASSWORD)
            _u = get_user(self.request)
            _dir = '{}.{}'.format(_u.username, int(timezone.now().timestamp()))
            # need to add a symbolic link from media to /etc/salt
            _srcdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/file/', _dir)
            _saltdir = 'salt://media/file/' + _dir
            os.makedirs(_srcdir)
            if not os.path.exists('/etc/salt/media'):
                os.symlink(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media'), '/etc/salt/media')
            for k, v in self.request.FILES.items():
                _f = File(file=v, uuid=uuid.uuid4(), user=_u, status=1)
                _f.save()
                _origin_fpath = _f.file.path
                _f.file.name = _f.file.name.replace('file/', 'file/{}/'.format(_dir))
                _f.save()
                shutil.move(_origin_fpath, _srcdir)
                _saltapi.remote_execution(arg=['{}/{}'.format(_saltdir, v.name), '{}/{}'.format(_dst_dir, v.name)],
                                          tgt=_glob, fun='cp.get_file')
            return Response('', status=status.HTTP_200_OK)
        return Response('Less glob and destination directory.', status=status.HTTP_400_BAD_REQUEST)
