#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午6:43
# @Author  : MiracleYoung
# @File    : entity.py

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from user.models import User, Group

__all__ = ['IDC', 'Entity']

class IDC(models.Model):
    name = models.CharField(_('IDC Name'), max_length=100, default='')
    idc_user = models.CharField(_('IDC User'), max_length=100, default='')
    idc_user_tel = models.CharField(_('IDC User Phone'), max_length=100, default='')
    user = models.ForeignKey(User, verbose_name=_('Department User'))
    address = models.CharField(_('IDC Address'), max_length=200, default='')
    create_time = models.DateTimeField(_('Create Time'), default=timezone.now())
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'asset_idc'
        ordering = ['name', ]

    def __str__(self):
        return '%s' % self.name

    __repr__ = __str__


class Entity(models.Model):
    STATUS_CHOICE = (
        (1, 'NORMAL'),
        (2, 'DELETED'),
        (3, 'Out of Service'),
    )

    ENV_CHOICES = (
        ('PRO', 'PRODUCTION'),
        ('GRAY', 'GRAY LEVEL'),
        ('STG', 'STAGE'),
        ('DEV', 'DEVELOPMENT'),
        ('TEST', 'TEST'),
    )
    # project related
    status = models.SmallIntegerField(_('Status'), choices=STATUS_CHOICE, default=1, blank=True)
    env = models.CharField(_('Environment'), max_length=100, choices=ENV_CHOICES, default='')
    owner = models.ForeignKey(User, verbose_name=_('Owner'))
    uuid = models.CharField(_('UUID'), max_length=100, default='', blank=True)
    # self related
    sn = models.CharField(_('Serial Number'), max_length=200, default='')
    cpu = models.CharField(_('CPU Info'), max_length=100, default='')
    memory = models.CharField(_('Memory Info'), max_length=100, default='')
    disk = models.CharField(_('Disk Info'), max_length=100, default='')
    hardware_version = models.CharField(_('Hardware Version'), max_length=200, default='', blank=True)
    # machined related
    idc = models.ForeignKey(IDC, on_delete=models.DO_NOTHING)
    cabinet = models.CharField(_('Cabinet'), max_length=100, default='', blank=True)
    detail_address = models.CharField(_('Detail Address like n U'), max_length=200, default='', blank=True)
    interface1 = models.CharField(_('Network Interface 1'), max_length=100, default='', blank=True)
    interface2 = models.CharField(_('Network Interface 2'), max_length=100, default='', blank=True)
    oob_ip = models.GenericIPAddressField(_('Out of Band Management IP'), default='0.0.0.0')
    oob_port = models.SmallIntegerField(_('Out of Band Management Port'), default=80, blank=True)
    oob_admin = models.CharField(_('Out of Band Management Admin Account'), max_length=100, default='', blank=True)
    oob_password = models.CharField(_('Out of Band Management Admin Password'), max_length=100, default='', blank=True)
    create_time = models.DateTimeField(_('Create Time'), default=timezone.now(), blank=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'asset_entity'
        ordering = ['create_time', ]

    def __str__(self):
        return 'Entity: <owner: %s>' % self.owner.username

    __repr__ = __str__
