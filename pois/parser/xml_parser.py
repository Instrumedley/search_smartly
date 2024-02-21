import xml.etree.ElementTree as ET
from .base_parser import BaseParser

class XmlParser(BaseParser):
    def parse(self):
        context = ET.iterparse(self.file_path, events=("start", "end"))
        _, root = next(context)
        for event, elem in context:
            if event == "end" and elem.tag == "DATA_RECORD":
                yield {
                    'id': elem.find('pid').text,
                    'name': elem.find('pname').text,
                    'category': elem.find('pcategory').text,
                    'latitude': float(elem.find('platitude').text),
                    'longitude': float(elem.find('plongitude').text),
                    'ratings': [float(rate) for rate in elem.find('pratings').text.split(",")]
                }
                root.clear()  # Clear processed elements to save memory
