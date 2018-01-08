from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
import datetime

__all__ = ['Token']

class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    token = models.CharField(_('Token'), max_length=128, default='')
    expire_time = models.DateTimeField(_('Expire Time'))
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)

    class Meta:
        db_table = 'token'


    def create(self, exp=7):
        self.expire_time = datetime.datetime.now() + datetime.timedelta(days=exp)
        return self

    def __str__(self):
        return 'token: %s' % self.token

    __repr__ = __str__