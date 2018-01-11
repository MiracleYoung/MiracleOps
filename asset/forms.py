#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:11
# @Author  : MiracleYoung
# @File    : forms.py

from django import forms
from .models.entity import IDC, Entity

__all__ = ['IDCForm', 'EntityForm']

class IDCForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', 'idc_user', 'idc_user_tel', 'user', 'address']


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'
        widgets = {
            'idc': forms.Select(),
            'status': forms.Select(),
            'env': forms.Select(),
        }
