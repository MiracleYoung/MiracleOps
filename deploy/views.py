from django.views.generic import ListView, TemplateView
from common.mixin import LoginRequiredMixin
import salt.client
import salt.key
from .models import SaltMinion


class SaltMinionListView(LoginRequiredMixin, TemplateView):
    template_name = 'deploy/salt_minion_list.html'

    def get_context_data(self, **kwargs):
        _minion_accept = SaltMinion.objects.filter(status=1)
        _minion_pre = SaltMinion.objects.filter(status=2)
        kwargs.update({
            'minion_accept': _minion_accept,
            'minion_pre': _minion_pre,
        })
        return super(SaltMinionListView, self).get_context_data(**kwargs)

class ExecuteCommandView(LoginRequiredMixin, ListView):
    template_name = 'deploy/execute_command.html'
    context_object_name = 'minion_list'

    def get_queryset(self):
        return SaltMinion.objects.all()
