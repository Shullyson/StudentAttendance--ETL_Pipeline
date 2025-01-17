from extract import extract_csv, extract_json, extract_xml, extract_excel
from transform import transform
from load import load_to_mysql
import pandas as pd
import json
import xml.etree.ElementTree as ET

DB_URI = ""

def main():
    # File paths
    csv_file = 'data/student_info.csv'
    json_file = 'data/attendance.json'
    xml_file = 'data/attendance.xml'
    excel_file = 'data/attendance.xlsx'
    
    # Extract
    student_data = extract_csv(csv_file)
    attendance_data_json = extract_json(json_file)
    attendance_data_xml = extract_xml(xml_file)
    attendance_data_excel = extract_excel(excel_file)
    
    # Transform
    student_data_transformed = transform(student_data)
    attendance_data_transformed = pd.concat([
        transform(attendance_data_json),
        transform(attendance_data_xml),
        transform(attendance_data_excel)
    ])
    
    # Load
    load_to_mysql(student_data_transformed, 'ETLStudents', DB_URI)
    load_to_mysql(attendance_data_transformed, 'ETLAttendance', DB_URI)

    print("ETL Process Completed Successfully")

if __name__ == "__main__":
    main()