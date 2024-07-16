from django.core.management.base import BaseCommand
from projectmanagement.models import User


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@pybase.net').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@pybase.net',
                password='123456',
                first_name='Pybase',
                last_name='Admin'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
