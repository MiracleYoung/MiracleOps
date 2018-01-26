#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/24 上午7:37
# @Author  : MiracleYoung
# @File    : str_handle.py

from django import template

register = template.Library()


@register.filter
def split(value: str, sep):
    return value.split(sep)


@register.filter
def index(value: list, idx):
    return value[idx]

@register.simple_tag
def retrieve_file_name(path: str):
    return path.split('/')[1]