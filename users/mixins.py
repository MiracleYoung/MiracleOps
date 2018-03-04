#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/3/4 上午6:57
# @Author  : MiracleYoung
# @File    : mixins.py


import datetime

from rest_framework import status
from django.shortcuts import redirect, reverse
from django.conf import settings
from django.http import HttpResponse


from .models import User, Token
from .authentication import verify_login_token




class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        _token = request.COOKIES.get('jwt', '')
        _ret, _payload = verify_login_token(_token)
        if _ret:
            _uid = _payload.get('sub', '')

            try:
                _t = Token.objects.get(token=_token)
            except Token.DoesNotExist:
                raise HttpResponse('token incorrect.', status=status.HTTP_404_NOT_FOUND)

            if _t.e_time == _payload.get('exp', ''):
                try:
                    _user = User.objects.get(_uid)
                except User.DoesNotExist:
                    raise HttpResponse('user incorrect.', status=status.HTTP_404_NOT_FOUND)

                if hasattr(request, 'user'):
                    request.user = _user
            # try:
            #     self.context = self.get_context_data(**kwargs)
            # except:
            #     self.context = {}
            # self.context['user'] = u
            # kwargs.update(self.context)
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            redirect_url = self.retrieve_redirect_url(request.path)
            return redirect(redirect_url)

    def retrieve_redirect_url(self, path, login_url=settings.LOGIN_URL):
        _login_url = reverse(login_url)
        return '{}?next={}'.format(_login_url, path)

    # def get(self, request, *args, **kwargs):
    #     _g = super().get(request, *args, **kwargs)
    #     _g.context_data.update(kwargs)
    #     context = _g.context_data
    #     return self.render_to_response(context)
