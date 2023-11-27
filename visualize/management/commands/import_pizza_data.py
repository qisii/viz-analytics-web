import csv
from django.core.management import BaseCommand
from visualize.models import PizzaHutLocation  

class Command(BaseCommand):
    help = 'Import Pizza Hut locations into PostgreSQL'

    def handle(self, *args, **options):
        file_path = 'dataset/pizza_hut_locations.csv'  # Update with the actual path to your dataset
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert empty values to None
                for field in ['type', 'address_1', 'address_2', 'open_hours', 'city', 'state', 'postal_code', 'latitude', 'longitude']:
                    row[field] = row[field] if row[field] != '' else None

                latitude = float(row['latitude']) if row['latitude'] is not None else None
                longitude = float(row['longitude']) if row['longitude'] is not None else None

                PizzaHutLocation.objects.create(
                    type=row['type'],
                    address_1=row['address_1'],
                    address_2=row['address_2'],
                    open_hours=row['open_hours'],
                    city=row['city'],
                    state=row['state'],
                    postal_code=row['postal_code'],
                    latitude=latitude,
                    longitude=longitude,
                )
        self.stdout.write(self.style.SUCCESS('Pizza Hut locations imported successfully'))