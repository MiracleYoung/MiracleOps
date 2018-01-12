#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 下午10:22
# @Author  : MiracleYoung
# @File    : entity.py

from rest_framework.serializers import ModelSerializer
from ..models import Entity, IDC

__all__ = ['EntitySerializer', 'IDCSerializer']


class EntitySerializer(ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class IDCSerializer(ModelSerializer):
    class Meta:
        model = IDC
        fields = '__all__'
