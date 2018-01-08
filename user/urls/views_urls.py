#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/5 下午7:55
# @Author  : MiracleYoung
# @File    : views.py

from django.conf.urls import url
from ..views.user import UserLoginView, UserCreateView

app_name = 'user'

urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(), name='login'),
    url(r'^register/$', UserCreateView.as_view(), name='register'),
]
