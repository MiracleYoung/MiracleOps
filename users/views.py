#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : models.py

from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse


class UserLoginView(TemplateView):
    template_name = "user/login.html"


class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        self.request.session.flush()
        return redirect(reverse('user:login'))
