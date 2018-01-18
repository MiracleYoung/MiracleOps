#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/18 11:24 AM
# @Author  : Miracle Young
# @File    : api_urls.py

from django.conf.urls import url
from .. import api

urlpatterns = [
    url(r'^minion-import/$', api.MinionImportApi.as_view(), name='minion-import'),
    url(r'^minion-check-alive/$', api.MinionCheckAliveApi.as_view(), name='minion-check-alive'),
    url(r'^minion/$', api.MinionApi.as_view(), name='minion'),
]
