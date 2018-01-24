#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/19/18 3:56 PM
# @Author  : Miracle Young
# @File    : math_filter.py

from django import template

register = template.Library()

@register.filter
def math_div(value, num):
    return value / num

@register.filter
def math_round(value, ndigits):
    return round(value, ndigits=ndigits)