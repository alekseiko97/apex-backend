import csv
import os
from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
    help = 'Import categories from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Skip the header row if present

            for row in reader:
                self.stdout.write(f'Reading row: {row}')

                # Skip empty rows
                if not row or all(not cell.strip() for cell in row):
                    self.stdout.write(self.style.WARNING('Skipping empty row'))
                    continue 

                id, name, parent_id = row  # Unpack the row into variables

                # Create or get the category
                category, _ = Category.objects.get_or_create(
                    #id = id,
                    defaults={
                        'name': name,
                    }
                )

                if parent_id:  # Check if parent_id is provided and not empty
                    parent_category, _ = Category.objects.get_or_create(id=parent_id)  # Only get the first value (Category instance)
                    category.parent_category = parent_category  # Assign the Category instance

                category.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported category: {category.name}'))