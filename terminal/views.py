from django.views.generic import TemplateView
from common.mixin import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'terminal/index.html'
