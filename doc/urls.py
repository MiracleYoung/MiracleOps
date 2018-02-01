#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/22 上午6:42
# @Author  : MiracleYoung
# @File    : urls.py

from django.conf.urls import url, include
from . import views

mo_url_patterns = [
    url(r'^list/', views.DocMOListView.as_view(), name='list', kwargs={'path2': 'List'}),

    url(r'^cm/', include([
        url(r'^exec-cmd/$', views.DocDeployExecCmdView.as_view(), name='exec-cmd'),
        url(r'^minion-list/$', views.DocDeployMinionListView.as_view(), name='minion-list'),
        url(r'^ssh/', views.DocSSHView.as_view(), name='ssh'),
        url(r'^sls/', views.DocSLSView.as_view(), name='sls'),
    ], namespace='cm'), kwargs={'path2': 'Deploy'}),

    url(r'^file/', include([
        url(r'^upload/$', views.DocSLSView.as_view(), name='upload'),
    ], namespace='file'), kwargs={'path2': 'File'}),
]

urlpatterns = [
    url(r'^mo/', include(mo_url_patterns, namespace='mo'), kwargs={'path1': 'MO'})

]
