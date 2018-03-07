#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/7/18 10:49 AM
# @Author  : Miracle Young
# @File    : user.py

from rest_framework import generics

from users.serializers import UserSerializer
from users.models import User
from common.mixins import LoginRequiredMixin


class UserListApi(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class UserDetailApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
