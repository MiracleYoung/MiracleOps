#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 3:14 PM
# @Author  : Miracle Young
# @File    : forms.py

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models.user import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'wechat', 'password']

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': _('Email'),
            'password': _('Password'),
        }

