#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/28/18 9:24 AM
# @Author  : Miracle Young
# @File    : v1.py

from django.conf.urls import url, include

from api.views.v1 import cm, asset, users

cms_patterns = [
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

assets_patterns = [
    url(r'^server/(?P<pk>[0-9a-f-]+)/$', asset.ServerApi.as_view(), name='server'),
    url(r'^idc/(?P<pk>[0-9a-f-]+)/$', asset.IDCApi.as_view(), name='idc'),
]

users_patterns = [
    url(r'^login/$', users.UserLoginApiView.as_view(), name='login'),
    url(r'^logout/$', users.UserLogoutApi.as_view(), name='logout'),
    url('^$', users.UserListApi.as_view(), name='list'),
    url('^(?P<pk>[0-9a-f-]+)/$', users.UserDetailApi.as_view(), name='detail'),
]


urlpatterns = [
    url(r'^cms/', include(cms_patterns, namespace='cms')),
    url(r'^assets/', include(assets_patterns, namespace='assets')),
    url(r'^users/', include(users_patterns, namespace='users')),
]
