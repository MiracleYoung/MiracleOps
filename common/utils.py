#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午8:57
# @Author  : MiracleYoung
# @File    : utils.py

from django.utils import timezone
from django.conf import settings
import hashlib

def gen_token(user, secret_key=settings.SECRET_KEY):
    '''
    token: md5(user_id:secret_key:timestamp)
    :param user:
    :param secret_key:
    :return:
    '''
    s = '%s:%s' % secret_key, timezone.now()
    token = hashlib.md5(s).hexdigest()
    return token
