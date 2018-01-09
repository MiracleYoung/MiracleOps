#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url
from ..views.entity import IDCView, EntityView, EntityCreateView, EntityDetailView

urlpatterns = [
    url(r'^idc/$', IDCView.as_view(), name='idc'),
    url(r'^entity/$', EntityView.as_view(), name='entity'),
    url(r'^entity/create/$', EntityCreateView.as_view(), name='entity-create', kwargs={'path1': 'Create'}),
    url(r'^entity/(?P<pk>\d+)/$', EntityDetailView.as_view(), name='entity-detail', kwargs={'path1': 'Detail'}),
]