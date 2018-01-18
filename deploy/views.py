from django.views.generic import ListView, TemplateView
from common.mixin import LoginRequiredMixin
import salt.client
import salt.key
from .models import SaltMinion


class SaltMinionListView(LoginRequiredMixin, TemplateView):
    template_name = 'deploy/salt_minion_list.html'

    def get_context_data(self, **kwargs):
        _salt_client = salt.client.LocalClient()
        _key_manager = salt.key.Key(_salt_client.opts)
        _all = _key_manager.all_keys()
        kwargs.update({
            '_minions_accept': _all['minions'],
            '_minions_denied': _all['minions_denied'],
            '_minions_unaccept': _all['minions_pre'],
            '_minions_reject': _all['minions_reject']
        })
        return super(SaltMinionListView, self).get_context_data(**kwargs)
