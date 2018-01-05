from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserProfileManager(BaseUserManager):
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


class UserProfile(AbstractBaseUser):
    email = models.EmailField('email address', max_length=128, unique=True)
    username = models.CharField('user name', max_length=32)
    wechat = models.CharField('wechat account', max_length=32, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['email', ], name = 'u_email_idx'),
        ]
        db_table = 'user_profile'

    objects = UserProfileManager()

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
