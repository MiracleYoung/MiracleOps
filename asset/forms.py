#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:11
# @Author  : MiracleYoung
# @File    : forms.py

from django import forms
from .models.entity_machine import IDC, EntityMachine


class IDCForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', 'idc_charge_user', 'idc_charge_user_tel', 'charge_user', 'address']


class EntityMachineForm(forms.ModelForm):
    class Meta:
        model = EntityMachine
        fields = ['idc', 'cabinet', 'detail_address', 'serial_number', 'interface1', 'interface2', 'owner',
                  'oob_management_admin', 'oob_management_ip', 'oob_management_password', 'oob_management_port']
