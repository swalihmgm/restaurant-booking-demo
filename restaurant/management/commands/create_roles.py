from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        admin_group,created = Group.objects.get_or_create(name='admin')
        customer_group,created = Group.objects.get_or_create(name='customer')

        self.stdout.write(
        self.style.SUCCESS("Roles created successfully")
        )