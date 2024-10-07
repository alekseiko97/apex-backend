from django.core.management.base import BaseCommand
from core.models import Organization

class Command(BaseCommand):
    help = 'Create a new organization.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Organization name')

    def handle(self, *args, **options):
        name = options['name']

        # Create organization
        organization = Organization.objects.create(
            name=name
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created organization: {organization.name}.'))
