import ijson
from .base_parser import BaseParser

class JsonParser(BaseParser):
    def parse(self):
        with open(self.file_path, 'rb') as jsonfile:
            for poi_data in ijson.items(jsonfile, 'item'):
                yield {
                    'id': poi_data['id'],
                    'name': poi_data['name'],
                    'category': poi_data['category'],
                    'latitude': poi_data['coordinates']['latitude'],
                    'longitude': poi_data['coordinates']['longitude'],
                    'ratings': poi_data['ratings']
                }
