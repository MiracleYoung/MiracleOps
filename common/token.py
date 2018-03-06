#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/6/18 9:36 AM
# @Author  : Miracle Young
# @File    : token.py

import time

from django.conf import settings
import jwt.exceptions

from users.models import User, Token


def gen_token(user: User):
    # generate login token
    _now = int(time.time())
    _expire_time = _now + 86400 * 7
    _payload = {
        "iss": "miracle",
        "iat": _now,
        "exp": _expire_time,
        "sub": user.id.hex,
        "role": user.role.name,
        "username": user.name
    }
    _token = jwt.encode(_payload, settings.SECRET_KEY, algorithm='HS256')
    try:
        _t = Token.objects.get(user=user)
        if token_is_expire(_t):
            # login token exist, then do not need to generate new token
            # return False
            return False, _token
    except Token.DoesNotExist:
        pass
    Token.objects.create(user=user, token=_token, e_time=_expire_time)
    return True, _token


def token_is_expire(token: Token):
    # True => not expire
    # False => expire => delete
    if token.e_time > int(time.time()):
        return True
    else:
        token.delete()
        return False


def verify_token(token):
    # verify token compliance
    try:
        _payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return True, _payload
    except jwt.exceptions.DecodeError:
        return False, {}
