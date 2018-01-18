from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from asset.models import Server


class SaltMinion(models.Model):
    STATUS_CHOICE = (
        (0, 'Unknown'),
        (1, 'Accepted'),
        (2, 'Unaccepted'),
        (3, 'Reject'),
        (4, 'Denied'),
    )

    hostname = models.CharField(_('Hostname'), max_length=100, default='')
    # when accept minion, need to initial server attr
    server = models.ForeignKey(Server, verbose_name=_('Server'), null=True)
    # minion salt key status
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=0)
    is_alive = models.BooleanField(_('Is Alive'))
    last_alive_time = models.DateTimeField(_('Last Alive Time'), null=True)
    # discover minion time
    discover_time = models.DateTimeField(_('Discover Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'deploy_salt_minion'
        ordering = ['discover_time', ]

    def __str__(self):
        return self.hostname

    __repr__ = __str__