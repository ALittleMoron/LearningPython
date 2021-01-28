import xml.etree.ElementTree as ET
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'sample.xml')


root = ET.parse(file_path)
print(root.getroot()[0][0].text)
