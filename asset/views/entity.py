#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:53
# @Author  : MiracleYoung
# @File    : entity.py

from django.views.generic import TemplateView, ListView, list, FormView, DetailView
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from common.mixin import LoginRequiredMixin
from ..models import IDC, Entity
from ..forms import *


class IDCView(LoginRequiredMixin, TemplateView):
    template_name = 'asset/idc.html'

    def get_context_data(self, **kwargs):
        context = {
            'idc_list': IDC.objects.all(),
        }
        kwargs.update(context)
        return super(IDCView, self).get_context_data(**kwargs)


class EntityView(LoginRequiredMixin, TemplateView):
    template_name = 'asset/entity.html'

    def get_context_data(self, **kwargs):
        context = {
            'entity_list': Entity.objects.all(),
        }
        kwargs.update(context)
        return super(EntityView, self).get_context_data(**kwargs)


class EntityCreateView(LoginRequiredMixin, FormView):
    template_name = 'asset/entity_create.html'
    form_class = EntityForm
    success_url = reverse_lazy('asset:entity')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(EntityCreateView, self).form_valid(form)


class EntityDetailView(LoginRequiredMixin, DetailView):
    model = Entity
    context_object_name = 'entity'
    template_name = 'asset/entity_detail.html'




