#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:53
# @Author  : MiracleYoung
# @File    : entity_machine.py

from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin

class IDCView(LoginRequiredMixin, TemplateView):
    template_name = 'asset/idc.html'