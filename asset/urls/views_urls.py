#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url, include

from asset import views

urlpatterns = [
    url(r'^idc/', include([
        url(r'^$', views.IDCListView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', views.IDCListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', views.IDCCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>\d+)/$', views.IDCDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', views.IDCUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='idc'), kwargs={'path1': 'IDC'}),
    url(r'^server/', include([
        url(r'^$', views.ServerListView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', views.ServerListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^(?P<pk>\d+)/$', views.ServerDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', views.ServerUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='server'), kwargs={'path1': 'Server'}),

]
