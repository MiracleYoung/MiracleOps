#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/12/2018 4:30 PM
# @Author  : Miracle Young
# @File    : server.py

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from user.models import User

__all__ = ['Server']

class Server(models.Model):
    STATUS_CHOICE = (
        (1, 'NORMAL'),
        (2, 'DELETED'),
        (3, 'Out of Service'),
    )

    ENV_CHOICE = (
        (1, 'Production'),
        (2, 'Gray Level'),
        (3, 'Stage'),
        (4, 'Development'),
        (5, 'Test'),
    )

    TYPE_CHOICE =(
        (1, 'Web Service'),
        (2, 'Database'),
        (3, 'Big Data'),
        (4, 'Middleware'),
        (5, 'Development'),
        (99, 'Other'),
    )

    host = models.CharField(_('Host'), max_length=100, default='')
    public_ip = models.GenericIPAddressField(_('Public IP'), default='0.0.0.0')
    private_ip1 = models.GenericIPAddressField(_('Private IP 1'), default='0.0.0.0')
    private_ip2 = models.GenericIPAddressField(_('Private IP 2'), default='0.0.0.0')
    private_ip3 = models.GenericIPAddressField(_('Private IP 3'), default='0.0.0.0')
    net_interface1 = models.CharField(_('Network Interface 1'), max_length=100, default='eth0')
    net_interface2 = models.CharField(_('Network Interface 2'), max_length=100, blank=True)
    net_interface3 = models.CharField(_('Network Interface 3'), max_length=100, blank=True)
    cpu = models.SmallIntegerField(_('CPU'), default=0)
    memory = models.SmallIntegerField(_('Memory'), default=0)
    disk = models.IntegerField(_('Disk'), default=0)

    env = models.SmallIntegerField(_('Environment'), choices=ENV_CHOICE, default=1)
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=1, blank=True)
    type = models.SmallIntegerField(_('Server Type'), choices=TYPE_CHOICE, default=1)

    owner = models.ForeignKey(User, verbose_name=_('Owner'))
    comment = models.CharField(_('Comment'), max_length=200, default='', blank=True)
    create_time = models.DateTimeField(_('Create Time'), default=timezone.now(), blank=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'asset_server'
        ordering = ['type']

    def __str__(self):
        return '%s:%s' % (self.host, self.ip)

    __repr__ = __str__