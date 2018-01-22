from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin


class GetHtmlPrefixMixin:
    def get_html_prefix(self, **kwargs):
        _html_name = self.request.path.replace('-', '_').split('/')
        _html_name.pop(0)
        _html_prefix = '_'.join(_html_name)
        return _html_prefix

    def get_context_data(self, **kwargs):
        kwargs['html_prefix'] = 'md/' + self.get_html_prefix() + '.md'
        return kwargs


class DocDeployExecuteCommandView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'


class DocDeployMinionListView(LoginRequiredMixin, GetHtmlPrefixMixin, TemplateView):
    template_name = 'doc/_doc.html'
