#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午8:57
# @Author  : MiracleYoung
# @File    : utils.py

from django.conf import settings
import hashlib
import datetime

def gen_token(user, secret_key=settings.SECRET_KEY):
    '''
    token: md5(user_id:secret_key:timestamp)
    :param user:
    :param secret_key:
    :return:
    '''
    s = '%s:%s' % (secret_key, str(datetime.datetime.now().timestamp() * 1000 * 1000))
    token = hashlib.md5(s.encode()).hexdigest()
    return token
