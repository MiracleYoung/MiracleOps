from django.views.generic import ListView, TemplateView, FormView
from django.urls import reverse_lazy
from django.utils import timezone
from common.mixin import LoginRequiredMixin
import salt.client
import salt.key
import uuid
from .models import *
from .forms import *
from user.models.user import User


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


class SaltSSHView(LoginRequiredMixin, FormView):
    template_name = 'deploy/salt_ssh.html'
    form_class = RosterForm
    success_url = reverse_lazy('deploy:ssh')

    def get_context_data(self, **kwargs):
        _ctx = super(SaltSSHView, self).get_context_data(**kwargs)
        _ctx['rosters'] = Roster.objects.all()
        return _ctx

    def form_valid(self, form):
        if form.is_valid():
            _u = User.objects.get(pk=self.request.session['uid'])
            file_name = '{}.{}.roster'.format(_u.username, int(timezone.now().timestamp()))
            form.instance.upload_to.name = file_name
            form.instance.uuid = uuid.uuid4()
            form.instance.user = _u
            form.instance.status = 1
            form.instance.file_name = file_name
            form.save()
            return super(SaltSSHView, self).form_valid(form)


