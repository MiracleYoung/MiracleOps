#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:11
# @Author  : MiracleYoung
# @File    : entity.py

from django import forms
from asset.models.entity import IDC, Entity

__all__ = ['IDCForm', 'EntityForm']


class IDCForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = '__all__'
        help_texts = {
            'name': '*required',
            'idc_user': '*required',
            'idc_user_tel': '*required',
            'user': '*required',
            'address': '*required',
        }


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'
        widgets = {
            'idc': forms.Select(),
            'status': forms.Select(),
            'env': forms.Select(),
        }
        help_texts = {
            'idc': '*required',
            'sn': '*required',
            'env': '*required',
            'owner': '*required',
            'cpu': '*required',
            'memory': '*required',
            'disk': '*required',
            'oob_ip': '*required',
        }
