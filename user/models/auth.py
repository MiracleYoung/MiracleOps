from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from ..models.user import User

class Token(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(_('Token'), max_length=128, default='')
    expire_time = models.IntegerField(_('Expire Time'), default=3600*24*7)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=now())
