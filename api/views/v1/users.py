#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/7/18 10:49 AM
# @Author  : Miracle Young
# @File    : user.py

from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import reverse

from users.serializers import UserRegisterSerializer, UserSerializer
from users.models import User, Role
from common.mixins import LoginRequiredMixin, JsonResponseMixin


class UserListApi(JsonResponseMixin, generics.ListCreateAPIView):
    serializer_class = UserRegisterSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid()
            _user = User.objects.create_user(**serializer.data)
            return self.json_response(0, {'url': reverse('users:login'), 'data': UserSerializer(_user).data},
                                  'Apply success. Please wait for you administrator confirm.')
        except ValueError as e:
            return self.json_response(1004, {}, str(e))


class UserDetailApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = UserRegisterSerializer

    def get_queryset(self):
        return User.objects.all()
