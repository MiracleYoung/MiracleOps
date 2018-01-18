#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午7:53
# @Author  : MiracleYoung
# @File    : server.py

from django.views.generic import ListView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from common.mixin import LoginRequiredMixin
from asset.models import IDC, Server
from asset.forms import ServerForm, IDCForm


class IDCListView(LoginRequiredMixin, ListView):
    template_name = 'asset/idc_list.html'
    model = IDC
    context_object_name = 'idc_list'

    def get_queryset(self):
        return IDC.objects.all()


class IDCCreateView(LoginRequiredMixin, FormView):
    template_name = 'asset/idc_create.html'
    form_class = IDCForm
    success_url = reverse_lazy('asset:idc:list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(IDCCreateView, self).form_valid(form)


class IDCDetailView(LoginRequiredMixin, DetailView):
    model = IDC
    context_object_name = 'idc'
    template_name = 'asset/idc_detail.html'


class IDCUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'asset/idc_update.html'
    model = IDC
    form_class = IDCForm
    success_url = reverse_lazy('asset:idc:list')


class ServerListView(LoginRequiredMixin, ListView):
    template_name = 'asset/server_list.html'
    model = Server
    context_object_name = 'server_list'

    def get_queryset(self):
        return super(ServerListView, self).get_queryset()


class ServerCreateView(LoginRequiredMixin, FormView):
    template_name = 'asset/server_create.html'
    form_class = ServerForm
    success_url = reverse_lazy('asset:server:list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ServerCreateView, self).form_valid(form)


class ServerDetailView(LoginRequiredMixin, DetailView):
    model = Server
    context_object_name = 'server'
    template_name = 'asset/server_detail.html'


class ServerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'asset/server_update.html'
    model = Server
    form_class = ServerForm
    success_url = reverse_lazy('asset:server:list')
