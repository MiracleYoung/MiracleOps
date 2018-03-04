import os, zipfile

from django.views.generic import ListView, TemplateView
from django.utils import timezone
from django.http import HttpResponseBadRequest, HttpResponse

from users.mixins import LoginRequiredMixin
from users.models import User
from .models import SaltMinion, Roster, Sls


class SaltMinionListView(LoginRequiredMixin, TemplateView):
    template_name = 'cm/minion_list.html'

    def get_context_data(self, **kwargs):
        _minion_accept = SaltMinion.objects.filter(status=1)
        _minion_pre = SaltMinion.objects.filter(status=2)
        kwargs.update({
            'minion_accept': _minion_accept,
            'minion_pre': _minion_pre,
        })
        return super(SaltMinionListView, self).get_context_data(**kwargs)


class SaltExecCmdView(LoginRequiredMixin, ListView):
    template_name = 'cm/exec_cmd.html'
    context_object_name = 'minion_list'

    def get_queryset(self):
        return SaltMinion.objects.all()


class SaltSSHView(LoginRequiredMixin, TemplateView):
    template_name = 'cm/salt_ssh.html'

    def get_context_data(self, **kwargs):
        _ctx = super(SaltSSHView, self).get_context_data(**kwargs)
        _ctx['rosters'] = Roster.objects.all()
        return _ctx

    def post(self, request, *args, **kwargs):
        _u = User.objects.get(pk=self.request.session['uid'])
        _f = self.request.FILES['file']
        if os.path.splitext(_f.name)[1] not in ('.roster'):
            return HttpResponseBadRequest('file must be like *.roster')
        _f.name = 'roster/{}_{}_{}'.format(_f.name, _u.username, int(timezone.now().timestamp()))
        _roster = Roster(file=_f, user=_u, status=1)
        _roster.save()
        return HttpResponse('')


class SaltSLSView(LoginRequiredMixin, TemplateView):
    template_name = 'cm/salt_sls.html'

    def get_context_data(self, **kwargs):
        _ctx = super(SaltSLSView, self).get_context_data(**kwargs)
        _ctx['slses'] = Sls.objects.all()
        return _ctx

    def post(self, request, *args, **kwargs):
        _u = User.objects.get(pk=self.request.session['uid'])
        _f = self.request.FILES['file']
        if os.path.splitext(_f.name)[1] not in ('.zip'):
            return HttpResponseBadRequest('file must be like *.zip')
        _f.name = 'sls/{}_{}_{}'.format(_f.name, _u.username, int(timezone.now().timestamp()))
        _sls = Sls(file=_f, user=_u, status=1)
        _sls.save()
        # whatever upload file type, mkdir <file>.dir, all in it
        _dir = _sls.file.path + '.dir'
        if not (os.path.exists(_dir) and os.path.isdir(_dir)):
            os.mkdir(_dir)
        # if zip, extract into <file>.dir, then remove zip
        if zipfile.is_zipfile(_sls.file):
            _z = zipfile.ZipFile(_sls.file.path)
            _z.extractall(_dir)
            os.remove(_sls.file.path)
        # if .sls, move into <file>.dir
        else:
            return HttpResponseBadRequest()
        return HttpResponse('')


class FileUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'cm/file_upload.html'
