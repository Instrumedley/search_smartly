import json
from .base_parser import BaseParser

class JsonParser(BaseParser):
    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            return [{
                'id': item['id'],
                'name': item['name'],
                'category': item['category'],
                'latitude': item['coordinates']['latitude'],
                'longitude': item['coordinates']['longitude'],
                'ratings': item['ratings']
            } for item in data]
