#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/7/18 10:49 AM
# @Author  : Miracle Young
# @File    : user.py

import datetime, hashlib, os, base64

from rest_framework import generics, views
from django.shortcuts import reverse, redirect

from users.serializers import UserRegisterSerializer, UserSerializer
from users.models import User, Token, VerifiedCode
from common.mixins import LoginRequiredMixin, JsonResponseMixin, CookieMixin


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
                _ret, _t = Token.gen_token(_user)
                _now = datetime.datetime.now()
                self.add_cookie(
                    **{'key': 'jwt', 'value': _t.token, 'expires': datetime.datetime.fromtimestamp(_t.e_time)})
                self.add_cookie(
                    **{'key': 'uid', 'value': _user.id, 'expires': datetime.datetime.fromtimestamp(_t.e_time)})
                _user.last_login = _now
                _user.save()
                _success_url = self.get_success_url()
                return self.json_response(0, {'url': _success_url, 'token': _t.token}, 'Login success.')
            else:
                return self.json_response(1002, '', 'Incorrect username and password.')

    def get_success_url(self):
        _referer = self.request.META.get('HTTP_REFERER', '')
        _, _, _next = _referer.partition('?')
        return _next.partition('=')[2] if _next else reverse('index')


class UserLogoutApi(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        self.request.session.flush()
        _token = request.META.get('HTTP_X_ACCESS_TOKEN', '') or request.COOKIES.get('jwt', '')
        Token.objects.get(token=_token).delete()
        return redirect(reverse('users:login'))


class UserRegisterApi(JsonResponseMixin, generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid()
            _user = User.objects.create_user(**serializer.data)
            _s = base64.b64encode(os.urandom(8))
            _m = hashlib.sha256()
            _m.update(_s)
            _code = VerifiedCode.objects.create(user=_user, code=_m.hexdigest(), type=1)
            return self.json_response(0, {'url': reverse('users:complete-info', kwargs={'code': _code.code}),
                                          'data': UserSerializer(_user).data},
                                      'Apply success. Please wait for you administrator confirm.')
        except ValueError as e:
            return self.json_response(1004, {}, str(e))


class UserDetailApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = UserRegisterSerializer
