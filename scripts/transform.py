import pandas as pd

def transform(dataframe):
    if "attendance_date" in dataframe.columns:  # Attendance data
        dataframe["student_id"] = dataframe["student_id"].astype(int)
        dataframe["attendance_date"] = pd.to_datetime(dataframe["attendance_date"])
        dataframe["status"] = dataframe["status"].str.capitalize()
    elif "name" in dataframe.columns:  # Student data
        dataframe["student_id"] = dataframe["student_id"].astype(int)
        dataframe["name"] = dataframe["name"].str.title()
        dataframe["gender"] = dataframe["gender"].str.capitalize()

    # Drop duplicates
    dataframe.drop_duplicates(inplace=True)

    return dataframe

