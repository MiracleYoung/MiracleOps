#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 上午11:54
# @Author  : MiracleYoung
# @File    : error.py

from rest_framework import status
from rest_framework.response import Response

def f_valid_required_err(form, **fields):
    for field, value in fields.items():
        if value is None:
            raise form.ValidationError('%s is required' % field.title())

def get_object_or_400(obj, pk):
    try:
        _obj = obj.objects.get(pk=pk)
    except:
        return Response('Oops, something wrong, please contact your administrator.', status=status.HTTP_400_BAD_REQUEST)
    return _obj