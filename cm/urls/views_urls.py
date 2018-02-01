#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/16 上午7:02
# @Author  : MiracleYoung
# @File    : views_urls.py

from django.conf.urls import url, include
from cm import views

urlpatterns = [
    url(r'^minion-list/$', views.SaltMinionListView.as_view(), name='minion-list', kwargs={'path1': 'Minion List'}),
    url(r'^exec-cmd/$', views.SaltExecCmdView.as_view(), name='exec-cmd', kwargs={'path1': 'Execute Command'}),
    url(r'^ssh/$', views.SaltSSHView.as_view(), name='ssh', kwargs={'path1': 'SSH'}),
    url(r'^sls/$', views.SaltSLSView.as_view(), name='sls', kwargs={'path1': 'SLS'}),
    url(r'^file-upload/$', views.FileUploadView.as_view(), name='file-upload', kwargs={'path1': 'File Upload'}),
]
