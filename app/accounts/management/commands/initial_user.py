from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Command(BaseCommand):
    help = 'Crea un super usuario'

    def handle(self, *args, **kwargs):
        """
        Comando que ayuda a crear un super usuario cuando
        se levanta el docker-compose de desarrollo
        """
        print("Creating superuser ...")
        user = CustomUser.objects.create_superuser(
            'worktion@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )
        print('User ' + user.email + " created")
