#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:11
# @Author  : MiracleYoung
# @File    : authentication.py

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password

from common.utils import gen_token
from common.error import get_object_or_400
from .models.user import User
from .serializers import UserSerializer


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