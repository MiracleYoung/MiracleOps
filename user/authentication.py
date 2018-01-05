#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:11
# @Author  : MiracleYoung
# @File    : authentication.py

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth.hashers import make_password, check_password

from common.utils import gen_token
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserCreateApi(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super(UserCreateApi, self).post(request, *args, **kwargs)


