#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:11
# @Author  : MiracleYoung
# @File    : authentication.py

import time

from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth.hashers import make_password
from django.conf import settings
import jwt.exceptions

from common.error import get_object_or_400
from .models import *
from .serializers import UserSerializer


def gen_login_token(user: User):
    _expire_time = int(time.time()) + 86400 * 7
    _payload = {
        "iss": "miracle",
        "iat": int(time.time()),
        "exp": _expire_time,
        "aud": "miracle",
        "sub": str(user.id),
        "role": user.role.role_name,
        "username": user.username,
    }
    _token = jwt.encode(_payload, settings.SECRET_KEY, algorithm='HS256')
    Token.objects.create(user=user, token=_token, e_time=_expire_time)
    return True, {'token': _token, 'uid': user.id}


def verify_login_token(token):
    try:
        _payload = jwt.decode(token, settings.SECRET_KEY, audience='miracle', algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        return False, {}
    return True, _payload


class UserRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super(UserCreateApi, self).post(request, *args, **kwargs)


def get_user(request):
    _uid = request.session['uid']
    return get_object_or_400(User, _uid)
