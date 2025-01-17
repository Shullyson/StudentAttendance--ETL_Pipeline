import pandas as pd
import json
import xml.etree.ElementTree as ET

def extract_csv(file_path):
    return pd.read_csv(file_path)

def extract_json(file_path):
    with open(file_path, 'r') as f:
        return pd.json_normalize(json.load(f))

def extract_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    records = []
    for record in root.findall('record'):
        records.append({
            'student_id': record.find('student_id').text,
            'attendance_date': record.find('attendance_date').text,
            'status': record.find('status').text
        })
    return pd.DataFrame(records)

def extract_excel(file_path):
    return pd.read_excel(file_path)
