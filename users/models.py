#!/usr/bin/env python
# encoding: utf-8
# @Time    : 1/5/2018 4:57 PM
# @Author  : Miracle Young
# @File    : models.py

import hashlib, os, base64, time, uuid

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, GroupManager, Permission
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import jwt

__all__ = ['User', 'Role', 'Token', 'Group', 'UserGroup']


class Role(models.Model):
    id = models.AutoField(_('ID'), primary_key=True)
    name = models.CharField(_('Role Name'), max_length=100, default='')
    c_time = models.DateTimeField(_('Create Time'), auto_now_add=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return 'Role: <{}>'.format(self.name)

    __repr__ = __str__


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        try:
            User.objects.get(email=email)
            raise ValueError('Email exist, please use another email.')
        except User.DoesNotExist:
            pass

        user = self.model(
            email=self.normalize_email(email),
            role=Role.objects.get(name='UnVerified')
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.role = Role.objects.get(name='Admin')
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    JOB_TITLE_CHOICE = (
        (0, 'Undefined'),
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

    id = models.UUIDField(_('ID'), default=uuid.uuid4, primary_key=True)
    email = models.EmailField(_('Email Address'), max_length=128, unique=True)
    phone = models.CharField(_('Mobile Phone Number'), max_length=20, default='')
    name = models.CharField(_('Name'), max_length=32, default='')
    wechat = models.CharField(_('WeChat Account'), max_length=32, default='')
    avatar = models.ImageField(_('Avatar'), upload_to='avatar', default='avatar/default_avatar.jpeg')
    job_title = models.SmallIntegerField(_('Job Title'), choices=JOB_TITLE_CHOICE, default=0)

    is_active = models.BooleanField(_('Is Active'), default=False)
    is_staff = models.BooleanField(_('Is Staff'), default=False)
    is_superuser = models.BooleanField(_('Is SuperUser'), default=False)

    role = models.ForeignKey('Role', verbose_name=_('Role'), null=True)

    reg_time = models.DateTimeField(_('Register Time'), auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['email', ], name='u_user_email'),
        ]
        db_table = 'user'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.name

    def get_avatar_url(self):
        return self.avatar.url

    def set_password(self, raw_password):
        # 8 length salt
        _salt = base64.b64encode(os.urandom(8))
        _m = hashlib.md5()
        _m.update(_salt + raw_password.encode())
        self.password = '{}${}'.format(_salt.decode(), _m.hexdigest())

    def check_password(self, raw_password):
        _salt, _password = self.password.split('$')
        _m = hashlib.md5()
        _m.update((_salt + str(raw_password)).encode())
        return _m.hexdigest() == _password

    def __str__(self):
        return '<User email: {}>'.format(self.email)

    __repr__ = __str__

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


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

    @staticmethod
    def gen_token(user: User):
        # generate login token
        try:
            _t = Token.objects.get(user=user)
            if not Token.token_is_expire(_t):
                # login token exist, then do not need to generate new token
                # return False
                return False, _t
        except Token.DoesNotExist:
            pass
        _now = int(time.time())
        _expire_time = _now + 86400 * 7
        _payload = {
            "iss": user.id.hex,
            "iat": _now,
            "exp": _expire_time,
            "sub": "login",
            "role": user.role.name,
            "username": user.name
        }
        _token = jwt.encode(_payload, settings.SECRET_KEY, algorithm='HS256')
        _t = Token.objects.create(user=user, token=_token, e_time=_expire_time)
        return True, _t

    @staticmethod
    def token_is_expire(token):
        # True => not expire
        # False => expire => delete
        if token.e_time > int(time.time()):
            return False
        else:
            token.delete()
            return True

    @staticmethod
    def verify_token(token):
        # verify token compliance
        try:
            _payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return True, _payload
        except jwt.exceptions.DecodeError:
            return False, {}


class Group(models.Model):
    id = models.AutoField(_('ID'), primary_key=True)
    name = models.CharField(_('name'), max_length=80, unique=True)
    c_time = models.DateTimeField(_('Create Time'), auto_now_add=True)

    class Meta:
        db_table = 'group'

    objects = GroupManager()

    def __str__(self):
        return '<Group: {}>'.format(self.name)

    __repr__ = __str__


class UserGroup(models.Model):
    id = models.AutoField(_('ID'), primary_key=True)
    user = models.ForeignKey(User, verbose_name=_('User'))
    group = models.ForeignKey(Group, verbose_name=_('Group'))

    class Meta:
        db_table = 'user_group'

    def __str__(self):
        return '<User: {}>: <Group: {}>'.format(self.user.name, self.group.name)

    __repr__ = __str__


class VerifiedCode(models.Model):
    TYPE_CHOICE = (
        (0, 'Undefined'),
        (1, 'Register Verified Code'),
    )

    id = models.AutoField(_('ID'), primary_key=True)
    user = models.ForeignKey(User, verbose_name=_('User'))
    code = models.CharField(_('Code'), max_length=200, default='')
    type = models.SmallIntegerField(_('Type'), choices=TYPE_CHOICE, default=0)
    c_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    u_time = models.DateTimeField(_('Update Time'), auto_now=True)

    class Meta:
        db_table = 'verified_code'

    def __str__(self):
        return '<{}: {}>'.format(self.user.name, self.code)

    __repr__ = __str__
