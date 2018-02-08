#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午6:43
# @Author  : MiracleYoung
# @File    : entity.py

import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from user.models import User, Group

__all__ = ['IDC', 'Server']

class IDC(models.Model):
    STATUS_CHOICE = (
        (1, 'NORMAL'),
        (2, 'DELETED'),
        (3, 'Out of Service'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_('IDC Name'), max_length=100, default='')
    idc_user = models.CharField(_('IDC User'), max_length=100, default='')
    idc_user_tel = models.CharField(_('IDC User Phone'), max_length=100, default='')
    user = models.ForeignKey(User, verbose_name=_('Department User'))
    address = models.CharField(_('IDC Address'), max_length=200, default='')
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=1, blank=True)
    c_time = models.DateTimeField(_('Create Time'), default=timezone.now(), blank=True)
    u_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'asset_idc'
        ordering = ['name', ]

    def __str__(self):
        return '%s' % self.name

    __repr__ = __str__


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
        (99, 'Other'),
    )

    TYPE_CHOICE = (
        (1, 'Web Service'),
        (2, 'Database'),
        (3, 'Big Data'),
        (4, 'Middleware'),
        (5, 'Development'),
        (99, 'Other'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    public_ip = models.GenericIPAddressField(_('Public IP'), default='0.0.0.0')
    # when first initial, if hostname is None or '', then hostname=public_ip
    hostname = models.CharField(_('Hostname'), max_length=100, default='', blank=True)
    private_ip1 = models.GenericIPAddressField(_('Private IP 1'), default='0.0.0.0')
    private_ip2 = models.GenericIPAddressField(_('Private IP 2'), default='0.0.0.0')
    os = models.CharField(_('OS'), max_length=100, default='')
    os_arch = models.CharField(_('OS Arch'), max_length=100, default='')
    # project related
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=1, blank=True)
    env = models.SmallIntegerField(_('Environment'), choices=ENV_CHOICE, default=1)
    type = models.SmallIntegerField(_('Server Type'), choices=TYPE_CHOICE, default=1)

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name=_('Owner'), null=True, db_constraint=False)
    # self related
    sn = models.CharField(_('Serial Number'), max_length=200, default='')
    cpu = models.SmallIntegerField(_('CPU'), default=0)
    memory = models.SmallIntegerField(_('Memory'), default=0)
    disk = models.CharField(_('Disk'), max_length=1000, default='')
    hardware_version = models.CharField(_('Hardware Version'), max_length=200, default='', blank=True)
    # machined related
    idc = models.ForeignKey(IDC, on_delete=models.DO_NOTHING, verbose_name=_('IDC'), null=True, db_constraint=False)
    cabinet = models.CharField(_('Cabinet'), max_length=100, default='', blank=True)
    cab_u = models.CharField(_('Cabinet U'), max_length=100, default='', blank=True)
    interface1 = models.SmallIntegerField(_('Network Interface 1'), default=0, blank=True)
    interface2 = models.SmallIntegerField(_('Network Interface 2'), default=0, blank=True)
    # oob
    oob_ip = models.GenericIPAddressField(_('Out of Band Management IP'), default='0.0.0.0')
    oob_port = models.SmallIntegerField(_('Out of Band Management Port'), default=80, blank=True)
    oob_admin = models.CharField(_('Out of Band Management Admin Account'), max_length=100, default='', blank=True)
    oob_password = models.CharField(_('Out of Band Management Admin Password'), max_length=100, default='', blank=True)

    remark = models.CharField(_('Remark'), max_length=200, default='', blank=True)
    c_time = models.DateTimeField(_('Create Time'), default=timezone.now(), blank=True)
    u_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'asset_server'
        ordering = ['c_time', ]

    def __repr__(self):
        return self.hostname

    __str__ = __repr__



