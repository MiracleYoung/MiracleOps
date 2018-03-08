#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:21
# @Author  : MiracleYoung
# @File    : serializers.py

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError("Email exists")
        except User.DoesNotExist:
            return email

    def create(self, validated_data):
        User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'job_title', 'is_active', 'is_superuser', 'role', 'last_login', 'reg_time',
                  'avatar',)
