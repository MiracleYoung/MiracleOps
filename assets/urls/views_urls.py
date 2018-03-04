#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url, include

from assets import views

urlpatterns = [
    url(r'^idc/', include([
        url(r'^list/$', views.IDCListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', views.IDCCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>[0-9a-f-]+)/$', views.IDCDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>[0-9a-f-]+)/update/$', views.IDCUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='idc'), kwargs={'path1': 'IDC'}),
    url(r'^server/', include([
        url(r'^list/$', views.ServerListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^(?P<pk>[0-9a-f-]+)/$', views.ServerDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>[0-9a-f-]+)/update/$', views.ServerUpdateView.as_view(), name='update',
            kwargs={'path2': 'Update'}),
    ], namespace='server'), kwargs={'path1': 'Server'}),

]
