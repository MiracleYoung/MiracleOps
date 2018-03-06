#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/7 下午3:43
# @Author  : MiracleYoung
# @File    : views.py

from django.views.generic import TemplateView

from common.mixins import LoginRequiredMixin, GetHtmlPrefixMixin


class DocMOListView(LoginRequiredMixin, TemplateView):
    template_name = 'doc/doc_mo_list.html'


class DocCMExecCmdView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocCMMinionListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocCMSSHView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocCMSLSView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocCMFileUploadView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocTerminalView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'
