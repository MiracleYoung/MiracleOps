#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : models.py

from django.views.generic import TemplateView
from django.http import Http404

from .models import VerifiedCode


class UserLoginView(TemplateView):
    template_name = "user/login.html"


class UserCompleteInfoView(TemplateView):
    template_name = 'user/complete_info.html'

    def get(self, request, *args, **kwargs):
        _code = kwargs.get('code', '')
        try:
            VerifiedCode.objects.get(code=_code, type=101)
            return super(UserCompleteInfoView, self).get(request, *args, **kwargs)
        except VerifiedCode.DoesNotExist:
            raise Http404()
