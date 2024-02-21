from .csv_parser import CsvParser
from .json_parser import JsonParser
from .xml_parser import XmlParser

'''Factory method to dynamically select and return an instance of the appropriate parser based on the file extension'''
def get_parser(file_path):
    if file_path.endswith('.csv'):
        return CsvParser(file_path)
    elif file_path.endswith('.json'):
        return JsonParser(file_path)
    elif file_path.endswith('.xml'):
        return XmlParser(file_path)
    else:
        raise ValueError("Unsupported file type!")
