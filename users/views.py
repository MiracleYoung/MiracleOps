#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : models.py

import datetime

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import redirect, reverse, render
from django import forms

from .forms import UserCreateForm, UserLoginForm
from .models import User
from .authentication import gen_login_token
from common.mixins import CookieMixin


class UserLoginView(CookieMixin, FormView):
    template_name = "user/login.html"
    form_class = UserLoginForm
    redirect_field_name = 'next'

    def form_valid(self, form):
        if form.is_valid():
            try:
                u = User.objects.get(email=form.cleaned_data['email'])
            except ObjectDoesNotExist:
                raise ValidationError('email does not exist')
            else:
                if u.check_password(form.cleaned_data['password']) and u.is_authenticated:
                    # get token and set token to cookie
                    _ret, _payload = gen_login_token(u)
                    _now = datetime.datetime.now()
                    if _ret:
                        self.add_cookie(
                            {'key': 'jwt', 'value': _payload, 'max_age': 86400 * 7, 'expires': _now, 'httponly': True})
                    u.last_login = _now
                    u.save()
                    return super(UserLoginView, self).form_valid(form)
                else:
                    raise ValidationError('password is incorrect.')

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
            except ObjectDoesNotExist:

                form.save()
                return render(self.request, 'user/login.html', {'message': 'Register successful, please login.'})


class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        self.request.session.flush()
        return redirect(reverse('user:login'))
