import argparse
from django.core.management.base import BaseCommand
from core.models import Organization, User

class Command(BaseCommand):
    help = 'Create a new user and add them to an organization.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the new user')
        parser.add_argument('email', type=str, help='Email for the new user')
        parser.add_argument('password', type=str, help='Password for the new user')
        parser.add_argument('organization_id', type=int, help='ID of the organization')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        organization_id = options['organization_id']

        # Fetch the organization
        try:
            organization = Organization.objects.get(id=organization_id)
        except Organization.DoesNotExist:
            self.stdout.write(self.style.ERROR('Organization not found.'))
            return

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            organization=organization  # Assign the organization
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username} in organization: {organization.name}.'))
