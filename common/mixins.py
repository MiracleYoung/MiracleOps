#!/usr/bin/env pythonAdd
# encoding: utf-8
# @Time    : 2018/1/6 上午7:55
# @Author  : MiracleYoung
# @File    : mixin.py

import datetime

from django.shortcuts import redirect, reverse
from django.conf import settings

from users.models import *


class CookieMixin:
    def __init__(self):
        self._cookies = []

    def get_cookies(self):
        return self._cookies

    def add_cookie(self, *args, **kwargs):
        self._cookies.append((*args, kwargs))

    def dispatch(self, request, *args, **kwargs):
        _res = super(CookieMixin, self).dispatch(request, *args, **kwargs)
        for _args, _kwargs in self.get_cookies():
            _res.set_cookie(*_args, **_kwargs)
        return _res





class GetHtmlPrefixMixin:
    def get_html_prefix(self, **kwargs):
        _html_name = self.request.path.replace('-', '_').split('/')
        _html_name.pop(0)
        _html_name.pop()
        _html_prefix = '_'.join(_html_name)
        return _html_prefix

    def get_context_data(self, **kwargs):
        kwargs['html_prefix'] = 'md/' + self.get_html_prefix() + '.md'
        return kwargs
