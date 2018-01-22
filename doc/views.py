from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin, GetHtmlPrefixMixin


class DocMOListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'

    def get_context_data(self, **kwargs):
        kwargs['html_prefix'] = 'doc/' + self.get_html_prefix() + '.html'
        return kwargs


class DocDeployExecuteCommandView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocDeployMinionListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'
