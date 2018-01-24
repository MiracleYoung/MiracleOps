#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/19/18 3:37 PM
# @Author  : Miracle Young
# @File    : serializer_filter.py

from django import template
import json

register = template.Library()

@register.filter
def json_loads(value):
    return json.loads(value)