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
        url(r'^exec-cmd/$', views.DocCMExecCmdView.as_view(), name='exec-cmd'),
        url(r'^minion-list/$', views.DocCMMinionListView.as_view(), name='minion-list'),
        url(r'^ssh/', views.DocCMSSHView.as_view(), name='ssh'),
        url(r'^sls/', views.DocCMSLSView.as_view(), name='sls'),
        url(r'^file-upload/$', views.DocCMFileUploadView.as_view(), name='file-upload'),
    ], namespace='cm'), kwargs={'path2': 'Cluster Management'}),

    url(r'^terminal/', views.DocTerminalView.as_view(), name='terminal', kwargs={'path2': 'Terminal'}),
]

urlpatterns = [
    url(r'^mo/', include(mo_url_patterns, namespace='mo'), kwargs={'path1': 'MO'})

]
