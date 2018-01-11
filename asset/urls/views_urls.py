#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url, include
from ..views.entity import IDCView, EntityView, EntityCreateView, EntityDetailView, EntityUpdateView

urlpatterns = [
    url(r'^idc/$', IDCView.as_view(), name='idc', kwargs={'path1': 'IDC'}),
    url(r'^entity/', include([
        url(r'^$', EntityView.as_view(), name='index', kwargs={'path2': 'Index'}),
        url(r'^list/$', EntityView.as_view(), name='list', kwargs={'path2': 'List'}),
        url(r'^create/$', EntityCreateView.as_view(), name='create', kwargs={'path2': 'Create'}),
        url(r'^(?P<pk>\d+)/$', EntityDetailView.as_view(), name='detail', kwargs={'path2': 'Detail'}),
        url(r'^(?P<pk>\d+)/update/$', EntityUpdateView.as_view(), name='update', kwargs={'path2': 'Update'}),
    ], namespace='entity'), kwargs={'path1': 'Entity'}),

]
