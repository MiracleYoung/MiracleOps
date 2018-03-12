#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/5 下午7:55
# @Author  : MiracleYoung
# @File    : views.py

from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^complete-info/(?P<code>[0-9a-f]+)$', views.UserCompleteInfoView.as_view(), name='complete-info'),
]
