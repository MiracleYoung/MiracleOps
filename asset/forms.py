#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:11
# @Author  : MiracleYoung
# @File    : entity.py

from django import forms

from asset.models import IDC, Server

__all__ = ['IDCForm', 'ServerForm']


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


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        widgets = {
            'idc': forms.Select(),
            'status': forms.Select(),
            'env': forms.Select(),
            'type': forms.Select(),
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
        'detail_address': 'If there are several u, enter like 22,23,24',
        'public_ip': '*required',
    }
