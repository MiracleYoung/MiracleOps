#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/8/2018 1:35 PM
# @Author  : Miracle Young
# @File    : views_urls.py

from django.conf.urls import url
from ..views.entity_machine import IDCView

urlpatterns = [
    url(r'^idc/$', IDCView.as_view(), name='idc'),
]