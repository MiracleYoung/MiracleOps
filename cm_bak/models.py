from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from asset.models import Server
from user.models.user import User

__all__ = ['SaltMinion', 'Roster', 'Sls']


class SaltMinion(models.Model):
    STATUS_CHOICE = (
        (0, 'Unknown'),
        (1, 'Accepted'),
        (2, 'Unaccepted'),
        (3, 'Reject'),
        (4, 'Denied'),
        (5, 'Deleted'),
    )

    hostname = models.CharField(_('Hostname'), max_length=100, default='')
    # when accept minion, need to initial server attr
    server = models.ForeignKey(Server, on_delete=models.DO_NOTHING, verbose_name=_('Server'), null=True)
    # minion salt key status
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=0)
    is_alive = models.BooleanField(_('Is Alive'))
    last_alive_time = models.DateTimeField(_('Last Alive Time'), null=True)
    # discover minion time
    discover_time = models.DateTimeField(_('Discover Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'cm_salt_minion'
        ordering = ['discover_time', ]

    def __repr__(self):
        return self.hostname

    __str__ = __repr__


class FileABC(models.Model):
    STATUS_CHOICE = (
        (0, 'Unknow'),
        (1, 'Normal'),
        (2, 'Deleted'),
    )

    uuid = models.CharField(_('UUID'), max_length=100, blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=0, blank=True)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(_('Update Time'), default=timezone.now(), null=True, blank=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.file.name

    __str__ = __repr__


class Roster(FileABC):
    file = models.FileField(_('File'), upload_to='roster/')

    class Meta:
        db_table = 'cm_roster'
        ordering = ['-create_time']


class Sls(FileABC):
    file = models.FileField(_('File'), upload_to='sls/')

    class Meta:
        db_table = 'cm_sls'
        ordering = ['-create_time']
