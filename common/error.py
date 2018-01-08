#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 上午11:54
# @Author  : MiracleYoung
# @File    : error.py



def f_valid_required_err(form, **fields):
    for field, value in fields.items():
        if value is None:
            raise form.ValidationError('%s is required' % field.title())