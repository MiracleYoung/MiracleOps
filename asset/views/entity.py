#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:53
# @Author  : MiracleYoung
# @File    : entity.py

from django.views.generic import TemplateView, ListView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from common.mixin import LoginRequiredMixin, GetMixin
from ..models import IDC, Entity
from ..forms import *


class IDCView(LoginRequiredMixin, GetMixin, ListView):
    template_name = 'asset/idc.html'
    model = IDC
    queryset = IDC.objects.all()
    context_object_name = 'idc_list'



class EntityView(LoginRequiredMixin, ListView):
    template_name = 'asset/entity.html'
    model = Entity
    context_object_name = 'entity_list'


class EntityCreateView(LoginRequiredMixin, FormView):
    template_name = 'asset/entity_create.html'
    form_class = EntityForm
    success_url = reverse_lazy('asset:entity:index')


class EntityDetailView(LoginRequiredMixin, DetailView):
    model = Entity
    context_object_name = 'entity'
    template_name = 'asset/entity_detail.html'


class EntityUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'asset/entity_update.html'
    model = Entity
    form_class = EntityForm
    success_url = reverse_lazy('asset:entity:index')
