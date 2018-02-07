from django.views.generic import TemplateView, ListView

from common.mixin import LoginRequiredMixin
from asset.models import *


class TerminalListView(LoginRequiredMixin, ListView):
    template_name = 'terminal/list.html'
    context_object_name = 'terminal_list'

    def get_queryset(self):
        return Server.objects.all()


class TerminalDetailView(LoginRequiredMixin, TemplateView):
    template_name = "terminal/detail.html"
