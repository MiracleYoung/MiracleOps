#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url, include
from ..views import entity, server

urlpatterns = [
    url(r'^idc/', include([
        url(r'^$', entity.IDCListView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', entity.IDCListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', entity.IDCCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>\d+)/$', entity.IDCDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', entity.IDCUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='idc'), kwargs={'path1': 'Entity'}),
    url(r'^entity/', include([
        url(r'^$', entity.EntityListView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', entity.EntityListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', entity.EntityCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>\d+)/$', entity.EntityDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', entity.EntityUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='entity'), kwargs={'path1': 'Entity'}),
    url(r'^server/', include([
        url(r'^$', server.ServerListView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', server.ServerListView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', server.ServerCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>\d+)/$', server.ServerDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', server.ServerUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='server'), kwargs={'path1': 'Server'}),
]
