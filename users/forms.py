#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 3:14 PM
# @Author  : Miracle Young
# @File    : entity.py

import re

from django import forms
from django.utils.translation import ugettext_lazy as _
from users.models import User

__all__ = ['UserCreateForm', 'UserLoginForm']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', "name", 'wechat', 'password', 'avatar', 'job_title', ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    @staticmethod
    def password_level(password):
        _weak = re.compile(r'^((\d+)|([A-Za-z]+)|(\W+))$')
        _middle = re.compile(r'([0-9]+(\W+|\_+|[A-Za-z]+))+|([A-Za-z]+(\W+|\_+|\d+))+|((\W+|\_+)+(\d+|\w+))+')
        _strong = re.compile(r'(\w+|\W+)+')
        if _weak.match(password):
            return 'weak'
        if _middle.match(password):
            return 'middle'
        if _strong.match(password):
            return 'strong'

    def clean_password(self):
        _password = self.cleaned_data.get('password')
        if UserCreateForm.password_level(_password) == 'strong':
            return _password
        else:
            raise forms.ValidationError('password is too simple, must contain letters,numbers,symbols.')

    def clean_avatar(self):
        _avatar = self.cleaned_data.get('avatar')
        if _avatar is None:
            _avatar = 'images/default_avatar.jpeg'
        return _avatar


class UserLoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=100)
    password = forms.CharField(label=_('Password'), max_length=100, strip=False)
