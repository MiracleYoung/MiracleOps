#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/22 上午6:42
# @Author  : MiracleYoung
# @File    : urls.py

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^deploy/', include([
        url(r'^execute-command', views.DocDeployExecuteCommandView.as_view(), name='execute-command', kwargs={'path2': 'Execute Command'}),
        url(r'^minion-list', views.DocDeployMinionListView.as_view(), name='minion-list', kwargs={'path2': 'Minion List'}),
    ], namespace='deploy'), kwargs={'path1': 'Deploy'}),
]