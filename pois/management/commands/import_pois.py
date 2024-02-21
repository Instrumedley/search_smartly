from django.core.management.base import BaseCommand
from pois.models import PointOfInterest
from django.contrib.gis.geos import Point
from pois.parser import get_parser

class Command(BaseCommand):
    help = 'Import Points of Interest from files'
    chunk_size = 100  # Number of records to be processed at a time, to avoid memory issues

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str, help='The file paths to import data from')

    def handle(self, *args, **options):
        self.stdout.write("Starting to extract data. This process may take a few minutes depending on"
                          "how large the files are \n", ending='')

        for file_path in options['files']:
            parser = get_parser(file_path)
            pois_to_create = []

            try:
                for poi_data in parser.parse():
                    location = Point(float(poi_data['longitude']), float(poi_data['latitude']), srid=4326)  # Ensure to set SRID if needed
                    pois_to_create.append(PointOfInterest(
                        id=poi_data['id'],
                        name=poi_data['name'],
                        category=poi_data['category'],
                        location=location,
                        ratings=poi_data['ratings']
                    ))
                    # Bulk insert when chunk size is reached
                    if len(pois_to_create) >= self.chunk_size:
                        PointOfInterest.objects.bulk_create(pois_to_create, ignore_conflicts=True)
                        pois_to_create = []
                        self.stdout.write(".", ending='')
                        self.stdout.flush()

                # Insert any remaining PoIs
                if pois_to_create:
                    PointOfInterest.objects.bulk_create(pois_to_create, ignore_conflicts=True)
                    self.stdout.write(".", ending='')
                    self.stdout.flush()

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing file {file_path}: {e}'))

        self.stdout.write("\n")  # Move to a new line after finishing all files
        self.stdout.write(self.style.SUCCESS('All records have been added successfully!'))
