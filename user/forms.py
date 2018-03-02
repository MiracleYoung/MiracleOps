#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 3:14 PM
# @Author  : Miracle Young
# @File    : entity.py

from django import forms
from django.utils.translation import ugettext_lazy as _
from user.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'wechat', 'password', 'avatar', 'job_title',]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if avatar is None:
            avatar = 'images/default_avatar.jpeg'
        return avatar

    def save(self, commit=True):
        self.instance.set_password(self.instance.password)
        return super(UserCreateForm, self).save(commit)


class UserLoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=100)
    password = forms.CharField(label=_('Password'), max_length=100, strip=False)


