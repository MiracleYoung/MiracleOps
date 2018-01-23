#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/23/18 2:31 PM
# @Author  : Miracle Young
# @File    : forms.py

from django import forms
from .models import *

__all__ = ['RosterForm', ]

class RosterForm(forms.ModelForm):
    class Meta:
        model = Roster
        fields = '__all__'
