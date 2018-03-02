#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:21
# @Author  : MiracleYoung
# @File    : serializers.py

from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
