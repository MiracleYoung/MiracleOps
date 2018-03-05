#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : models.py

import datetime

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse, render
from django import forms

from .forms import UserCreateForm, UserLoginForm
from .models import User
from api.views.v1.auth import gen_login_token
from common.mixins import CookieMixin


class UserLoginView(CookieMixin, FormView):
    template_name = "user/login.html"
    form_class = UserLoginForm
    redirect_field_name = 'next'

    def form_valid(self, form):
        if form.is_valid():
            _email = form.cleaned_data.get('email', '')
            try:
                _user = User.objects.get(_email)
            except User.DoesNotExist:
                return render(self.request, 'user/login.html', {'message': 'Email {} does not exist.'.format(_email)})
            else:
                _password = form.cleaned_data.get('password', '')
                if _user.check_password(_password) and _user.is_authenticated:
                    # get token and set token to cookie
                    _ret, _payload = gen_login_token(u)
                    _now = datetime.datetime.now()
                    if _ret:
                        self.add_cookie(
                            {'key': 'jwt', 'value': _payload, 'max_age': 86400 * 7, 'expires': _now, 'httponly': True})
                    _user.last_login = _now
                    _user.save()
                    return super(UserLoginView, self).form_valid(form)
                else:
                    return render(self.request, 'user/login.html', {'message': 'Incorrect email and password.'})

    def get_success_url(self):
        _referer = self.request.META.get('HTTP_REFERER', '')
        _, _, _next = _referer.partition('?')
        return _next.partition('=')[2] if _next else reverse('index')


class UserCreateView(FormView):
    template_name = "user/register.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        if form.is_valid():
            try:
                User.objects.get(email=form.cleaned_data['email'])
                raise forms.ValidationError('Email exist, please change another one.')
            except User.ObjectDoesNotExist:
                form.save()
                return form


class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        self.request.session.flush()
        return redirect(reverse('user:login'))
