#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 4:57 PM
# @Author  : Miracle Young
# @File    : user.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

__all__ = ['User']

class UserManager(BaseUserManager):
    def create_user(self, email, username, wechat, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            wechat = wechat,
            is_staff = True,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, wechat=None, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            wechat = wechat,
            password = password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    JOB_TITLE = (
        ('DBA', 'Database Administrator'),
        ('SA', 'System Administrator'),
        ('NA', 'Network Administrator'),
        ('IT', 'Help Desk/IT'),
        ('Director', 'Director'),
        ('Manager', 'Manager'),
        ('TL', 'Tech Leader'),
    )

    email = models.EmailField(_('Email Address'), max_length=128, unique=True)
    username = models.CharField(_('User Name'), max_length=32)
    wechat = models.CharField(_('WeChat Account'), max_length=32, blank=True)
    avatar = models.ImageField(_('Avatar'), upload_to='avatar', null=True, blank=True, default='avatar/default_avatar.jpeg')
    job_title = models.CharField(_('Job Title'), max_length=32, choices=JOB_TITLE, default='', blank=True)
    reg_time = models.DateTimeField(_('Register Time'), auto_now_add=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_admin = models.BooleanField(_('Is Admin'), default=False)
    is_staff = models.BooleanField(_('Is Staff'), default=True)

    class Meta:
        indexes = [
            models.Index(fields=['email', ], name = 'u_email_idx'),
        ]
        db_table = 'user'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    __repr__ = __str__

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    # @property
    # def is_staff(self):
    #     return self.is_staff



# from django.contrib.auth.tokens import default_token_generator
#
# default_token_generator.make_token(user=u)
