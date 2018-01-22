#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/11/2018 9:50 AM
# @Author  : Miracle Young
# @File    : url.py

from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def url_reverse(*args, **kwargs):
    try:
        return reverse(':'.join([v.lower() for v in args]))
    except:
        return reverse(':'.join([v.lower() for v in args[:-1]]))


@register.filter
def reverse_space2dash(value: str):
    return '-'.join(value.split())
