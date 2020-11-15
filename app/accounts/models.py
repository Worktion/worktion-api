from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, username, **extra_fields):
        if not email:
            raise ValueError(_('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name, username, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must hav is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, first_name, last_name, username, **extra_fields)


class CustomUser(AbstractUser):
    """ Custum user model """
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(_('user name'), null=True, blank=True, max_length=150)
    bio = models.TextField(_('user biography'), blank=True, null=True)
    birth_date = models.DateField(_('user birthday'), blank=True, null=True)
    cover = models.ImageField(upload_to='users-cover', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = CustomUserManager()
