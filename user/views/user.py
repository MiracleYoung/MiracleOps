#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : user.py

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, reverse, render
from django import forms
from django.utils import timezone
from user.forms import UserLoginForm, UserCreateForm
from ..models.user import User
from common.utils import gen_token
import datetime


class UserLoginView(FormView):
    template_name = "user/login.html"
    form_class = UserLoginForm
    redirect_field_name = 'next'

    def form_valid(self, form):
        if form.is_valid():
            try:
                u = User.objects.get(email=form.cleaned_data['email'])
            except ObjectDoesNotExist:
                form.add_error('email', 'email does not exist')
                return render(self.request, 'user/login.html', {'form': form})
            else:
                if u.check_password(form.cleaned_data['password']) and u.is_authenticated:
                    # create token
                    # add token, token_exp, uid to request.session
                    self.request.session['uid'] = u.id
                    self.request.session['token'] = gen_token(u)
                    self.request.session['token_exp'] = (timezone.now() + datetime.timedelta(days=7)).timestamp()
                    u.last_login = timezone.now()
                    u.save()
                    return super(UserLoginView, self).form_valid(form)
                else:
                    form.add_error('password', 'password is incorrect.')
                    return render(self.request, 'user/login.html', {'form': form})

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