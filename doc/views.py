from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin, GetHtmlPrefixMixin


class DocMOListView(LoginRequiredMixin, TemplateView):
    template_name = 'doc/doc_mo_list.html'


class DocDeployExecCmdView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocDeployMinionListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocSSHView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocSLSView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'
