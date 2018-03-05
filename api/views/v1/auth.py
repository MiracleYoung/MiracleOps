#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:11
# @Author  : MiracleYoung
# @File    : auth.py

import time, datetime

from rest_framework import generics, views, status
from django.conf import settings
import jwt.exceptions

from common.error import get_object_or_400
from common.mixins import CookieMixin
from users.models import User, Token
from users.serializers import UserSerializer, UserLoginSerializer
from ..base import BaseAPIView


def gen_login_token(user: User):
    _expire_time = int(time.time()) + 86400 * 7
    _payload = {
        "iss": "miracle",
        "iat": int(time.time()),
        "exp": _expire_time,
        "aud": "miracle",
        "sub": user.id.hex,
        "role": user.role.name,
        "username": user.name,
    }
    _token = jwt.encode(_payload, settings.SECRET_KEY, algorithm='HS256').decode()
    Token.objects.create(user=user, token=_token, e_time=_expire_time)
    return True, {'token': _token, 'uid': user.id.hex}


def verify_login_token(token):
    try:
        _payload = jwt.decode(token, settings.SECRET_KEY, audience='miracle', algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        return False, {}
    return True, _payload


class UserLoginApiView(CookieMixin, BaseAPIView):
    def post(self, request, *args, **kwargs):
        _email = request.data.get('email')
        _password = request.data.get('password')
        try:
            _user = User.objects.get(email=_email)
        except User.DoesNotExist:
            return self.json_response(1001, '', 'User does not exist.')
        else:
            if _user.check_password(_password) and _user.is_authenticated:
                # get token and set token to cookie
                _ret, _payload = gen_login_token(_user)
                _now = datetime.datetime.now()
                if _ret:
                    self.add_cookie(**{'key': 'jwt', 'value': _payload, 'max_age': 86400 * 7, 'expires': _now})
                _user.last_login = _now
                _user.save()
                return self.json_response(0, '', 'Login success.')
            else:
                return self.json_response(1002, '', 'Incorrect username and password.')


class UserRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # request.data['password'] = make_password(request.data['password'])
        return super(UserCreateApi, self).post(request, *args, **kwargs)
