#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/7/18 10:49 AM
# @Author  : Miracle Young
# @File    : user.py

from rest_framework import generics
from django.shortcuts import reverse

from users.serializers import UserSerializer
from users.models import User
from common.mixins import LoginRequiredMixin, JsonResponseMixin


class UserListApi(JsonResponseMixin, generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    # def post(self, request, *args, **kwargs):
    #     _email = request.data.get('email', '')
    #     _password = request.data.get('password', '')
    #     _serializer = UserSerializer(data=request.data)
    #     _serializer.is_valid()
    #     return self.json_response(0, {'url': reverse('users:login'), 'data': _serializer.data},
    #                                   'Apply success. Please wait for your administrator confirm.')
    
    def post(self, request, *args, **kwargs):
        return super(UserListApi, self).post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.create()


class UserDetailApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
