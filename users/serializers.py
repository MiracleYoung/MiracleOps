#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:21
# @Author  : MiracleYoung
# @File    : serializers.py

from rest_framework import serializers

from .models import User, Role, Job

__all__ = ['UserRegisterSerializer', 'UserInfoSerializer', 'UserSerializer', 'RoleSerializer', 'JobSerializer']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)

    def validate_email(self, email):
        # TODO
        return email


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'wechat', 'phone', 'job', 'avatar',)

    def validate_name(self, name):
        if name.strip() and isinstance(name, str) and len(name) <= 32:
            return name
        else:
            raise serializers.ValidationError('Name is invalid.')

    def validate_wechat(self, wechat):
        if wechat.strip() and isinstance(wechat, str) and len(wechat) <= 32:
            return wechat
        else:
            raise serializers.ValidationError('Wechat is invalid.')

    def validate_phone(self, phone):
        if phone.strip() and isinstance(phone, str) and len(phone) <= 20:
            return phone
        else:
            raise serializers.ValidationError('Phone is invalid.')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name', 'job', 'is_active', 'is_superuser', 'role', 'last_login',
                  'reg_time', 'avatar',)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name',)
