from django.core.management.base import BaseCommand, CommandError
from pois.models import PointOfInterest
from pois.parser import get_parser
import os

class Command(BaseCommand):
    help = 'Imports Points of Interest from specified files'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str, help='The file paths to import data from')

    def handle(self, *args, **options):
        for file_path in options['file_paths']:
            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(f'File {file_path} does not exist'))
                continue

            try:
                parser = get_parser(file_path)
                pois = parser.parse()

                for poi_data in pois:
                    poi, created = PointOfInterest.objects.update_or_create(
                        id=poi_data['id'],
                        defaults={
                            'name': poi_data['name'],
                            'category': poi_data['category'],
                            'location': f"POINT({poi_data['longitude']} {poi_data['latitude']})",
                            'description': poi_data.get('description', ''),
                            'ratings': poi_data['ratings'],
                        }
                    )

                    action = 'Created' if created else 'Updated'
                    self.stdout.write(self.style.SUCCESS(f"{action} {poi.name} with ID {poi.id}"))

            except Exception as e:
                raise CommandError(f'Error importing {file_path}: {e}')

            self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {file_path}'))
