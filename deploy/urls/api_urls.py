#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/18/18 11:24 AM
# @Author  : Miracle Young
# @File    : api_urls.py

from django.conf.urls import url
from .. import api

urlpatterns = [
    url(r'^minion-refresh/$', api.MinionRefreshApi.as_view(), name='minion-refresh'),
    url(r'^minion-check-alive/$', api.MinionCheckAliveApi.as_view(), name='minion-check-alive'),
    url(r'^minion/(?P<pk>\d+)/$', api.MinionApi.as_view(), name='minion'),
    url(r'^execute-cmd/$', api.ExecuteCommand.as_view(), name='execute-cmd'),
]
