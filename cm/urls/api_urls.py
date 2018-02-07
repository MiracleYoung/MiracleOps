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
    url(r'^minion/(?P<pk>[0-9a-f-]+)/$', api.MinionApi.as_view(), name='minion'),
    url(r'^minion-cmd/$', api.MinionCmdApi.as_view(), name='minion-cmd'),
    url(r'^roster/(?P<pk>[0-9a-f-]+)/$', api.RosterApi.as_view(), name='roster'),
    url(r'^install-minion/(?P<roster_id>[0-9a-f-]+)/$', api.InstallMinionApi.as_view(), name='install-minion'),
    url(r'^ssh-cmd/$', api.SSHCmdApi.as_view(), name='ssh-cmd'),
    url(r'^sls/(?P<pk>[0-9a-f-]+)/$', api.SLSApi.as_view(), name='sls'),
    url(r'^sls/$', api.SLSCmdApi.as_view(), name='sls-cmd'),
    url(r'^file-upload/$', api.FileUploadApi.as_view(), name='file-upload'),
]
