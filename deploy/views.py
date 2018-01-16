from django.views.generic import ListView, TemplateView
from common.mixin import LoginRequiredMixin

class SaltMinionListView(LoginRequiredMixin, TemplateView):
    template_name = 'deploy/salt_minion_list.html'


