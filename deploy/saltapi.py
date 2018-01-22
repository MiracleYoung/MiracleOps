#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/18 10:24 AM
# @Author  : Miracle Young
# @File    : saltapi.py

# coding:utf8
import urllib, json
import urllib.request
import urllib.parse
import requests


# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context


class SaltAPI(object):
    __token_id = ''

    def __init__(self, url, username, password):
        self.__url = url.rstrip('/')
        self.__user = username
        self.__password = password

    def token_id(self):
        """
        用户登陆和获取token
        """
        data = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        content = self.post_request(data, prefix='/login')
        try:
            self.__token_id = content['return'][0]['token']
        except KeyError:
            raise KeyError

    def post_request(self, data, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token': self.__token_id}
        req = requests.post(url, json=data, headers=headers)
        return req.json()

    def get_request(self, data, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token': self.__token_id}
        req = requests.get(url, json=data, headers=headers)
        return req.json()

    def list_all_key(self):
        """
        获取包括认证、未认证salt主机
        """
        data = {'client': 'wheel', 'fun': 'key.list_all'}
        self.token_id()
        content = self.post_request(data)
        minions = content['return'][0]['data']['return']['minions']
        minions_pre = content['return'][0]['data']['return']['minions_pre']
        return minions, minions_pre

    def delete_key(self, match, mul=False):
        '''
        拒绝salt主机
        '''
        fun = 'key.delete'
        if mul:
            fun = 'key.delete_dict'
            if not isinstance(match, dict):
                return 'match variables must be dict.'
        data = {'client': 'wheel', 'fun': fun, 'match': match}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]['data']['success']
        return ret

    def accept_key(self, match, mul=False):
        '''
        接受salt主机
        '''
        fun = 'key.accept'
        if mul:
            fun = 'key.accept_dict'
            if not isinstance(match, list):
                return 'match variables must be dict.'
            match = {"minions_pre": match}
        data = {'client': 'wheel', 'fun': fun, 'match': match}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]['data']['success']
        return ret

    def salt_get_jid_ret(self, jid):
        '''
        通过jid获取执行结果
        '''
        data = {'client': 'runner', 'fun': 'jobs.lookup_jid', 'jid': jid}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def salt_get_running_jobs(self):
        '''
        获取运行中的任务
        '''
        data = {'client': 'runner', 'fun': 'jobs.active'}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def salt_check_alive(self, tgt):
        '''
        salt主机存活检测
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': 'test.ping'}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def remote_one_server(self, tgt, fun):
        '''
        获取单一主机信息
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0][tgt]
        return ret

    def remote_execution(self, tgt, fun, tgt_type='glob', arg=None):
        ''' 执行命令有参数 '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'tgt_type': tgt_type}
        if arg:
            data['arg'] = arg
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def salt_get_minions_ret(self, tgt, fun, tgt_type='glob', arg=None):
        data = {'tgt': ','.join(tgt), 'fun': fun, 'tgt_type': tgt_type}
        if arg:
            data['arg'] = arg
        self.token_id()
        content = self.post_request(data, '/minions')
        return content

    def remote_execution_module(self, tgt, fun, arg, tgt_type='glob'):
        '''
        异步执行远程命令、部署模块
        '''
        data = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'list', 'tgt_type': tgt_type}
        self.token_id()
        content = self.post_request(data)
        jid = content['return'][0]['jid']
        return jid

    def remote_localexec(self, tgt, fun, arg):
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'list'}
        self.token_id()
        content = self.post_request(data)
        print(content)
        ret = content['return'][0]
        return ret

    def salt_state(self, tgt, arg, expr_form):
        '''
        sls文件
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg, 'expr_form': expr_form}
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def project_manage(self, tgt, fun, arg1, arg2, arg3, arg4, arg5, expr_form):
        '''
        文件上传、备份到minion、项目管理
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        # 拼接url参数
        data2 = {'arg': arg2}
        arg_add = urllib.parse.urlencode(data2)
        data = urllib.parse.urlencode(data).encode('utf-8')
        data = data + '&' + arg_add
        data3 = {'arg': arg3}
        arg_add = urllib.parse.urlencode(data3)
        data = data + '&' + arg_add
        data4 = {'arg': arg4}
        arg_add = urllib.parse.urlencode(data4)
        data = data + '&' + arg_add
        data5 = {'arg': arg5}
        arg_add = urllib.parse.urlencode(data5)
        data = data + '&' + arg_add
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def file_copy(self, tgt, fun, arg1, arg2, expr_form):
        '''
        文件上传、备份到minion、项目管理
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        # 拼接url参数
        data2 = {'arg': arg2}
        arg_add = urllib.parse.urlencode(data2)
        data = urllib.parse.urlencode(data).encode('utf-8')
        data = data + '&' + arg_add
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def file_bak(self, tgt, fun, arg, expr_form):
        '''
        文件备份到master
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': expr_form}
        data = urllib.parse.urlencode(data).encode('utf-8')
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret

    def file_manage(self, tgt, fun, arg1, arg2, arg3, expr_form):
        '''
        文件回滚
        '''
        data = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg1, 'expr_form': expr_form}
        data2 = {'arg': arg2}
        arg_add = urllib.parse.urlencode(data2)
        data = urllib.parse.urlencode(data).encode('utf-8')
        data = data + '&' + arg_add
        data3 = {'arg': arg3}
        arg_add_2 = urllib.parse.urlencode(data3)
        data = data + '&' + arg_add_2
        self.token_id()
        content = self.post_request(data)
        ret = content['return'][0]
        return ret
