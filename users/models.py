#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 4:57 PM
# @Author  : Miracle Young
# @File    : models.py

import hashlib, os, base64, time

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

__all__ = ['User', 'Role', 'Token']


class UserManager(BaseUserManager):
    def create_user(self, email, username, wechat, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            wechat=wechat
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, wechat=None, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            wechat=wechat,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    JOB_TITLE_CHOICE = (
        (1, 'Database Administrator'),
        (2, 'System Administrator'),
        (3, 'Network Administrator'),
        (4, 'Help Desk/IT'),
        (5, 'Developer'),
        (6, 'Tester'),

        (101, 'Director'),
        (102, 'Manager'),
        (103, 'Tech Leader'),

    )

    email = models.EmailField(_('Email Address'), max_length=128, unique=True)
    username = models.CharField(_('User Name'), max_length=32)
    wechat = models.CharField(_('WeChat Account'), max_length=32, blank=True)
    avatar = models.ImageField(_('Avatar'), upload_to='avatar', null=True, blank=True,
                               default='avatar/default_avatar.jpeg')
    job_title = models.SmallIntegerField(_('Job Title'), choices=JOB_TITLE_CHOICE, default=0, blank=True)

    is_active = models.BooleanField(_('Is Active'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=True)
    is_superuser = models.BooleanField(_('Is SuperUser'), default=False)

    role = models.ForeignKey('Role', verbose_name=_('Role'))

    reg_time = models.DateTimeField(_('Register Time'), auto_now_add=True)
    login_time = models.DateTimeField(_('Login Time'), default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['email', ], name='u_email_idx'),
        ]
        db_table = 'user'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def set_password(self, raw_password):
        # 8 length salt
        _salt = base64.b64encode(os.urandom(8))
        _m = hashlib.md5()
        _m.update(_salt + raw_password.encode())
        self.password = '{}${}'.format(_salt.decode(), _m.hexdigest())

    def check_password(self, raw_password):
        _salt, _password = self.password.split('$')
        _m = hashlib.md5()
        return _m.update(_salt + raw_password.encode()).hexdigest() == _password

    def __str__(self):
        return self.email

    __repr__ = __str__

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Role(models.Model):
    id = models.AutoField(_('ID'), primary_key=True)
    role_name = models.CharField(_('Role Name'), max_length=100, default='')

    class Meta:
        db_table = 'role'

    def __str__(self):
        return 'Role: <{}>'.format(self.role_name)

    __repr__ = __str__


class Token(models.Model):
    id = models.AutoField(_('ID'), primary_key=True)
    user = models.ForeignKey('User', verbose_name=_('User'))
    token = models.CharField(_('Token'), max_length=1024, default='')
    c_time = models.IntegerField(_('Create Time'), default=int(time.time()))
    e_time = models.IntegerField(_('Expire Time'), default=int(time.time()) + 86400 * 7)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return 'Token: <{}>'.format(self.token)

    __repr__ = __str__
