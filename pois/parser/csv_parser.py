import csv
from .base_parser import BaseParser
class CsvParser(BaseParser):
    def parse(self):
        pois = []
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pois.append({
                    'id': row['poi_id'],
                    'name': row['poi_name'],
                    'category': row['poi_category'],
                    'latitude': float(row['poi_latitude']),
                    'longitude': float(row['poi_longitude']),
                    'ratings': [float(rate) for rate in row['poi_ratings'].strip("{}").split(",")]
                })
        return pois
