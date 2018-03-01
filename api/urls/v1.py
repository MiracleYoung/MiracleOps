#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/28/18 9:24 AM
# @Author  : Miracle Young
# @File    : v1.py

from django.conf.urls import url, include

from ..views.v1 import cm, asset

cm_patterns = [
    url(r'^minion-refresh/$', cm.MinionRefreshApi.as_view(), name='minion-refresh'),
    url(r'^minion-check-alive/$', cm.MinionCheckAliveApi.as_view(), name='minion-check-alive'),
    url(r'^minion/(?P<pk>[0-9a-f-]+)/$', cm.MinionApi.as_view(), name='minion'),
    url(r'^minion-cmd/$', cm.MinionCmdApi.as_view(), name='minion-cmd'),
    url(r'^roster/(?P<pk>[0-9a-f-]+)/$', cm.RosterApi.as_view(), name='roster'),
    url(r'^install-minion/(?P<roster_id>[0-9a-f-]+)/$', cm.InstallMinionApi.as_view(), name='install-minion'),
    url(r'^ssh-cmd/$', cm.SSHCmdApi.as_view(), name='ssh-cmd'),
    url(r'^sls/(?P<pk>[0-9a-f-]+)/$', cm.SLSApi.as_view(), name='sls'),
    url(r'^sls-cmd/$', cm.SLSCmdApi.as_view(), name='sls-cmd'),
    url(r'^file-upload/$', cm.FileUploadApi.as_view(), name='file-upload'),
]

asset_patterns = [
    url(r'^server/(?P<pk>[0-9a-f-]+)/$', asset.ServerApi.as_view(), name='server'),
    url(r'^idc/(?P<pk>[0-9a-f-]+)/$', asset.IDCApi.as_view(), name='idc'),
]

urlpatterns = [
    url(r'^cm/', include(cm_patterns, namespace='cm')),
    url(r'^asset/', include(asset_patterns, namespace='asset')),
]
