from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserM


#class CustomUser(AbstractUser):
#    username = None
#    email = models.EmailField(unique=True)
#
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = []
#
#    objects = CustomUserM()
#
#    def __str__(self):
#        return self.email


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserM()

    def __str__(self):
        return self.email