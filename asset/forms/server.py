#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/12/2018 4:41 PM
# @Author  : Miracle Young
# @File    : server.py

from django import forms
from ..models import Server

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        help_texts = {
            'host': '*required',
            'public_ip': '*required',
            'private_ip1': '*required',
            'net_interface1': '*required',
            'env': '*required',
            'type': '*required',
            'owner': '*required',
            'cpu': '*required. For example: 8',
            'memory': '*required. For example: 16(unit G)',
            'disk': '*required. For example: 200(unit G)',
        }
        widgets = {
            'env': forms.Select(),
            'type': forms.Select(),
            'status': forms.Select(),
        }