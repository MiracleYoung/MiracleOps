#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/3 下午9:12
# @Author  : MiracleYoung
# @File    : urls.py

from django.conf.urls import url
from user.authentication import UserRetrieveUpdateDestroyApi

app_name = 'user'

urlpatterns = [
    url(r'^(?P<pk>[0-9])/$', UserRetrieveUpdateDestroyApi.as_view(), name='retrieve-update-destroy'),
]