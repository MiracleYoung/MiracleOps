from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import Http404, HttpResponseBadRequest
from common.mixin import LoginRequiredMixin
import uuid, os, zipfile, shutil
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


class SaltExecCmdView(LoginRequiredMixin, ListView):
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
            _f_name = self.request.FILES['file'].name
            if os.path.splitext(_f_name) not in ('.roster'):
                return HttpResponseBadRequest('file must be like *.roster')
            file_name = '{}_{}_{}'.format(_f_name, _u.username, int(timezone.now().timestamp()))
            form.instance.file.name = file_name
            form.instance.uuid = uuid.uuid4()
            form.instance.user = _u
            form.instance.status = 1
            form.save()
            return super(SaltSSHView, self).form_valid(form)
        return HttpResponseBadRequest()


class SaltSLSView(LoginRequiredMixin, FormView):
    template_name = 'deploy/salt_sls.html'
    form_class = SlsForm
    success_url = reverse_lazy('deploy:sls')

    def get_context_data(self, **kwargs):
        _ctx = super(SaltSLSView, self).get_context_data(**kwargs)
        _ctx['slses'] = Sls.objects.all()
        return _ctx

    def form_valid(self, form):
        if form.is_valid():
            _u = User.objects.get(pk=self.request.session['uid'])
            _f_name = self.request.FILES['file'].name
            if os.path.splitext(_f_name)[1] not in ('.zip'):
                return HttpResponseBadRequest('file must be like *.zip')
            file_name = '{}_{}_{}'.format(_f_name, _u.username, int(timezone.now().timestamp()))
            form.instance.file.name = file_name
            form.instance.uuid = uuid.uuid4()
            form.instance.user = _u
            form.instance.status = 1
            form.save()

            _file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/sls/', file_name)
            _dir = _file + '.dir'
            # whatever upload file type, mkdir <file>.dir, all in it
            if not (os.path.exists(_dir) and os.path.isdir(_dir)):
                os.mkdir(_dir)
            # if zip, extract into <file>.dir, then remove zip
            if zipfile.is_zipfile(form.instance.file):
                _z = zipfile.ZipFile(form.instance.file.path)
                _z.extractall(_dir)
                os.remove(_file)
            # if .sls, move into <file>.dir
            else:
                return HttpResponseBadRequest()
            return super(SaltSLSView, self).form_valid(form)
        return HttpResponseBadRequest()


class FileUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'deploy/file_upload.html'
