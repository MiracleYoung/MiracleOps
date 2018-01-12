#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/12/2018 4:43 PM
# @Author  : Miracle Young
# @File    : server.py

from django.views.generic import ListView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from common.mixin import LoginRequiredMixin
from ..models import Server
from ..forms import ServerForm


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