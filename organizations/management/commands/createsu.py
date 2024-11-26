# users/management/commands/createsu.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'osc_user'
        email = 'oscadmin@gmail.com'
        password = 'oscuseroscsite'

        if not User.objects.filter(username=username).exists():
            self.stdout.write('Creating superuser...')
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write('Superuser created.')
        else:
            self.stdout.write('Superuser already exists.')
