#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : models.py

import datetime

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django import forms

from .forms import UserCreateForm
from .models import User


class UserLoginView(TemplateView):
    template_name = "user/login.html"


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
