"""
Enterprise Data Trust Score Platform

File : validator.py

Purpose:
Contains reusable validation functions
for checking enterprise data quality.
"""

import pandas as pd


def check_missing_values(df):
    """
    Count missing values in each column.
    """

    return df.isnull().sum()

def check_duplicate_rows(df):
    """
    Count duplicate rows in the dataset.
    """

    return int(df.duplicated().sum())

def check_duplicate_employee_id(df):
    """
    Count duplicate Employee IDs.
    """

    return int(df["Employee_ID"].duplicated().sum())

def check_invalid_salary(df):
    """
    Count employees having invalid salary.
    """

    invalid_salary = df[
        (df["Salary"] < 25000) |
        (df["Salary"] > 120000)
    ]

    return int(len(invalid_salary))

def check_invalid_department(df):
    """
    Count employees having invalid departments.
    """

    valid_departments = [
        "Human Resources",
        "Finance",
        "Sales",
        "Marketing",
        "IT",
        "Operations"
    ]

    invalid_department = df[
        ~df["Department"].isin(valid_departments)
    ]

    return int(len(invalid_department))

def check_future_joining_date(df):
    """
    Count employees having future joining dates.
    """

    temp_df = df.copy()

    temp_df["Joining_Date"] = pd.to_datetime(
        temp_df["Joining_Date"]
    )

    future_date = temp_df[
        temp_df["Joining_Date"] > pd.Timestamp.today()
    ]

    return int(len(future_date))

def generate_validation_report(df):
    """
    Generate complete validation report.
    """

    report = {
        "Missing Values": check_missing_values(df).sum(),
        "Duplicate Rows": check_duplicate_rows(df),
        "Duplicate Employee ID": check_duplicate_employee_id(df),
        "Invalid Salary": check_invalid_salary(df),
        "Invalid Department": check_invalid_department(df),
        "Future Joining Date": check_future_joining_date(df)
    }

    return report