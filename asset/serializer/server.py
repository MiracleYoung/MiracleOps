#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/12 下午7:42
# @Author  : MiracleYoung
# @File    : server.py

from rest_framework.serializers import ModelSerializer
from ..models import Server

__all__ = ['ServerSerializer']


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'
