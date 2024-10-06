import csv
from django.core.management.base import BaseCommand
from core.models import Product, Category  # Adjust the import based on your app structure

class Command(BaseCommand):
    help = 'Import products from a CSV file'

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

                sku, name, ean, url, category_1, category_2, category_3 = row  # Unpack the row into variables

                # Handle missing EAN by assigning a placeholder
                if not ean:
                    self.stdout.write(self.style.WARNING('Provided empty EAN, filling in with placeholder value'))
                    ean = f"UNKNOWN-{sku}"  # Use the SKU to generate a unique EAN placeholder
                
                # Create or get categories
                category1 = self.get_first_or_create(name=category_1)
                category2 = self.get_first_or_create(name=category_2)
                category3 = self.get_first_or_create(name=category_3)

                # Create or get the product
                product, created = Product.objects.get_or_create(
                    sku=sku,
                    defaults={
                        'name': name,
                        'ean': ean,
                        'url': url,
                    }
                )

                # Assign categories to the product
                product.categories.add(category1, category2, category3)
                product.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported product: {product.name}'))

    # Define the helper function to get the first category by name or create it
    def get_first_or_create(self, name):
        if name:  # Ensure the category name is provided
            # Try to get the first matching category by name
            category = Category.objects.filter(name=name).first()
            if not category:
                # If no such category exists, create it
                category = Category.objects.create(name=name)
            return category
        return None
