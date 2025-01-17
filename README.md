# Project Readme: ETL Pipeline for Student Attendance Data

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline for managing student attendance data. It demonstrates how to handle various data formats, transform them for consistency, and load them into a MySQL database. While the system is designed to work with actual student data, synthetic data is used for this demonstration.

For security purposes, the database connection link has been excluded from the repository. Users can set up their own database and create the required tables as outlined below.

---

## Project Structure

```
project-directory/
|
├── data/               # Directory containing input data files
│   ├── student_info.csv
│   ├── attendance.json
│   ├── attendance.xml
│   ├── attendance.xlsx
│
├── extract.py          # Script to extract data from various file formats
├── transform.py        # Script to transform data for consistency
├── load.py             # Script to load data into the MySQL database
├── main.py             # Main script to execute the ETL pipeline
├── test.py             # Script to test database connection
├── requirements.txt    # Python dependencies for the project
└── read.txt            # Project documentation (this file)
```

---

## Setting Up the Project

### Prerequisites
- Python 3.7+
- MySQL database
- Required Python libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

### Database Setup
1. **Create a MySQL database:**
   ```sql
   CREATE DATABASE StudentAttendance;
   ```

2. **Create the necessary tables:**
   ```sql
   CREATE TABLE ETLStudents (
       student_id INT PRIMARY KEY,
       name VARCHAR(100),
       gender VARCHAR(10)
   );

   CREATE TABLE ETLAttendance (
       student_id INT,
       attendance_date DATE,
       status VARCHAR(50),
       PRIMARY KEY (student_id, attendance_date)
   );
   ```

3. **Set up the database URI:**
   Update the `DB_URI` variable in `main.py` and `test.py` with your database credentials:
   ```python
   DB_URI = "mysql+pymysql://username:password@host:port/StudentAttendance"
   ```

### Synthetic Data
The project uses synthetic data located in the `data/` directory. Replace these files with actual data as needed while maintaining the same structure.

---

## Running the Project
1. **Test the database connection:**
   Run the `test.py` script to ensure the database is accessible:
   ```bash
   python test.py
   ```

2. **Run the ETL pipeline:**
   Execute the `main.py` script to process and load data:
   ```bash
   python main.py
   ```

---

## Security Considerations
- **Database Credentials:** The database connection URI has been omitted from the project for security reasons. Use environment variables or a secure secrets manager to store credentials.
- **Data Privacy:** Ensure that any actual student data used complies with relevant data protection regulations (e.g., GDPR, FERPA).

---

## Notes
- The synthetic data in the `data/` directory is for demonstration purposes. Replace these files with actual data to use the pipeline in a real-world scenario.
- The `DB_URI` in `main.py` and `test.py` must be updated with valid credentials before running the scripts.
- Ensure the required tables exist in the database before running the ETL process.
