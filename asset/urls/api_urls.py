#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:38 PM
# @Author  : Miracle Young
# @File    : api_urls.py

from django.conf.urls import url, include
from ..api import *

urlpatterns = [
    url(r'^server/(?P<pk>\d+)/$', ServerDetailApi.as_view(), name='server-detail'),
    url(r'^idc/(?P<pk>\d+)/$', IDCDetailApi.as_view(), name='idc-detail'),
]
