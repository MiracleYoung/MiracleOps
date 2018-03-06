#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:11
# @Author  : MiracleYoung
# @File    : auth.py

import datetime

from rest_framework import generics, views
from django.shortcuts import reverse

from users.models import User
from users.serializers import UserSerializer
from common.mixins import CookieMixin, JsonResponseMixin
from common.token import gen_token


class UserLoginApiView(CookieMixin, JsonResponseMixin, views.APIView):
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
                _ret, _token = gen_token(_user)
                _now = datetime.datetime.now()
                if _ret:
                    self.add_cookie(**{'key': 'jwt', 'value': _token, 'max_age': 86400 * 7, 'expires': _now})
                _user.last_login = _now
                _user.save()
                _success_url = self.get_success_url()
                return self.json_response(0, {'url': _success_url, 'token': _token}, 'Login success.')
            else:
                return self.json_response(1002, '', 'Incorrect username and password.')

    def get_success_url(self):
        _referer = self.request.META.get('HTTP_REFERER', '')
        _, _, _next = _referer.partition('?')
        return _next.partition('=')[2] if _next else reverse('index')


class UserRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # request.data['password'] = make_password(request.data['password'])
        return super(UserCreateApi, self).post(request, *args, **kwargs)
