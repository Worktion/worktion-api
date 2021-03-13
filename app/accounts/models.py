import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from utils.email import Email
from datetime import timedelta


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
        user.send_email_confirmation()
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
    email_verified = models.BooleanField(default=False)
    token_confirmation_email = models.UUIDField(default=uuid.uuid4, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = CustomUserManager()

    @classmethod
    def login(cls, email, password):
        """ Method to get access to the system """
        if not email:
            raise ValueError('The email must be set')
        if not password:
            raise ValueError('The password must be set')
        exist_email = CustomUser.objects.filter(email=email).exists()
        if not exist_email:
            raise ValueError('email not found')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            # (refresh)
            new_access_token = refresh.access_token
            new_access_token.set_exp(lifetime=timedelta(seconds=30))
            if not user.email_verified:
                raise ValueError(_('email has not yet been verified'))
            return {
                'email_verified': user.email_verified,
                'refresh': str(refresh),
                'access': str(new_access_token),
            }
        else:
            raise ValueError('User or password incorrect')

    def send_email_confirmation(self):
        try:
            token = AccessToken.for_user(self)
            token.set_exp(lifetime=timedelta(days=30))
            print(token)
            Email.send_confirmation_register(self, token)
        except Exception as ex:
            raise ex

    def validate_email(self):
        self.email_verified = True
        self.save()
