import xml.etree.ElementTree as ET
from .base_parser import BaseParser
class XmlParser(BaseParser):
    def parse(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        pois = []
        for record in root.findall('DATA_RECORD'):
            pois.append({
                'id': record.find('pid').text,
                'name': record.find('pname').text,
                'category': record.find('pcategory').text,
                'latitude': float(record.find('platitude').text),
                'longitude': float(record.find('plongitude').text),
                'ratings': [float(rate) for rate in record.find('pratings').text.split(",")]
            })
        return pois
