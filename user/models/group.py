#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/11/2018 11:24 AM
# @Author  : Miracle Young
# @File    : group.py

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['Group']

class Group(models.Model):
    NAME_CHOICE = (
        ('DB', 'Database'),
        ('SYS', 'System'),
        ('NE', 'Network'),
        ('IT', 'IT Information'),
        ('LAB', 'LAB'),
        ('SE', 'Security'),
    )
    name = models.CharField(_('Group Name'), choices=NAME_CHOICE, max_length=100)
    perm = models.CharField(_('Permission'), max_length=100, default='')

    class Meta:
        db_table = 'group'
        ordering = ['name', ]

    def __str__(self):
        return '%s' % self.name

    __repr__ = __str__
