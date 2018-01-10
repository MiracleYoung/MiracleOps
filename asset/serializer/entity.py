#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 下午10:22
# @Author  : MiracleYoung
# @File    : entity.py

from rest_framework.serializers import ModelSerializer
from ..models import Entity

__all__ = ['EntitySerializer']

class EntitySerializer(ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

    def update(self, instance, validated_data):
        entity = Entity.objects.get(validated_data['pk'])