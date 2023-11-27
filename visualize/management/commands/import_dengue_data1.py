import csv
from datetime import datetime
from django.core.management import BaseCommand
from visualize.models import Dengue

class Command(BaseCommand):
    help = 'Import dengue data into PostgreSQL'

    def handle(self, *args, **options):
        file_path = 'dataset/doh-epi-dengue-data-2016-2021 (1).csv'  # Update with the actual path to your dataset
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Skip rows with invalid values
                # if row['loc'].startswith('#') or row['deaths'] == '':
                #     continue
                if row['loc'].startswith('#'):
                    continue

                Dengue.objects.create(
                    loc=row['loc'],
                    cases=int(row['cases']),
                    deaths=int(row['deaths']),
                    date=datetime.strptime(row['date'], '%Y-%m-%d').date(),
                    region=row['Region']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))