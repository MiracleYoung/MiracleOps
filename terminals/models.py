import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from assets.models import Server
from users.models import User

__all__ = ['Terminal', ]


# one record one session
class Terminal(models.Model):
    STATUS_CHOICE = (
        (0, 'CLOSED'),
        (1, 'ESTABLISHED'),
        (2, 'ERROR'),
    )

    id = models.UUIDField(_('ID'), default=uuid.uuid4, primary_key=True)
    server = models.ForeignKey(Server, verbose_name=_('Server'), db_constraint=False)
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=0)
    ssh_port = models.SmallIntegerField(_('SSH Port'), default=22)
    user = models.ForeignKey(User, verbose_name=_('User'), db_constraint=False, null=True)
    t_id = models.CharField(_('Thread ID'), max_length=100, default='')
    c_time = models.DateTimeField(_('Create Time'), default=timezone.now)
    u_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'terminal'

    def __repr__(self):
        return '{}:{}'.format(self.server.hostname, self.ssh_port)

    __str__ = __repr__
