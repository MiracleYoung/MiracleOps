from django.views.generic import TemplateView, ListView
from django.db.models import Count

from common.mixin import LoginRequiredMixin
from asset.models import *


class TerminalListView(LoginRequiredMixin, ListView):
    template_name = 'terminal/list.html'
    context_object_name = 'terminal_list'

    def get_queryset(self):
        return Server.objects.values('id', 'hostname', 'public_ip').annotate(cn=Count('terminal__id'))


class TerminalDetailView(LoginRequiredMixin, TemplateView):
    template_name = "terminal/detail.html"
