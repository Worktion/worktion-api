from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        print("Creating superuser ...")
        user = User.objects.create_superuser('admin', 'worktion@gmail.com', 'contraseñafuerte')
        print('User ' + user.username + " created")