from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin, GetHtmlPrefixMixin


class DocMOListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocDeployExecuteCommandView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocDeployMinionListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'
