#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 上午6:43
# @Author  : MiracleYoung
# @File    : entity_machine.py

from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models.user import User

__all__ = ['IDC', 'EntityMachine']

class IDC(models.Model):
    name = models.CharField(_('IDC Name'), max_length=100, default='')
    idc_charge_user = models.CharField(_('IDC Charge User'), max_length=100, default='')
    idc_charge_user_tel = models.CharField(_('IDC Charge User Mobile Phone'), max_length=100, default='')
    charge_user = models.OneToOneField(User, verbose_name=_('Department Charge User'))
    address = models.CharField(_('IDC Address'), max_length=200, default='')

    class Meta:
        db_table = 'asset_idc'

    def __str__(self):
        return 'IDC: <%s>' % self.name

    __repr__ = __str__


class EntityMachine(models.Model):
    idc = models.ForeignKey(IDC, on_delete=models.DO_NOTHING)
    cabinet = models.CharField(_('Cabinet'), max_length=100, default='')
    detail_address = models.CharField(_('Detail Address like n U'), max_length=200, default='')
    serial_number = models.CharField(_('Serial Number'), max_length=200, default='')
    interface1 = models.CharField(_('Network Interface 1'), max_length=100, default='')
    interface2 = models.CharField(_('Network Interface 2'), max_length=100, default='')
    owner = models.OneToOneField(User, verbose_name=_('Owner'))
    oob_management_ip = models.GenericIPAddressField(_('Out of Band Management IP'), default='0.0.0.0')
    oob_management_port = models.SmallIntegerField(_('Out of Band Management Port'), default=80)
    oob_management_admin = models.CharField(_('Out of Band Management Admin Account'), max_length=100, default='')
    oob_management_password = models.CharField(_('Out of Band Management Admin Password'), max_length=100, default='')

    class Meta:
        db_table = 'asset_entity_machine'

    def __str__(self):
        return 'EntityMachine: <owner: %s>' % self.owner.username

    __repr__ = __str__
