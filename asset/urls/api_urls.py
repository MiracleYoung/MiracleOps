#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:38 PM
# @Author  : Miracle Young
# @File    : api_urls.py

from django.conf.urls import url, include
from .. import api

urlpatterns = [
    url(r'^server/(?P<pk>\d+)/$', api.ServerApi.as_view(), name='server'),
    url(r'^idc/(?P<pk>\d+)/$', api.IDCApi.as_view(), name='idc'),
]
