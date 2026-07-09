"""
Enterprise Data Trust Score Platform

Module : database.py

Purpose:
Manage SQLite database operations.
"""

import sqlite3
import pandas as pd

def create_connection():
    """
    Create SQLite database connection.
    """

    connection = sqlite3.connect("database/enterprise_data.db")

    return connection

def create_employee_table(connection):

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(

        Employee_ID INTEGER PRIMARY KEY,
        First_Name TEXT,
        Last_Name TEXT,
        Email TEXT,
        Phone TEXT,
        Department TEXT,
        Job_Title TEXT,
        Salary INTEGER,
        Joining_Date TEXT,
        City TEXT,
        Trust_Score INTEGER,
        Trust_Category TEXT

    )
    """)

    connection.commit()

def load_employee_data(connection, dataframe):
    """
    Load employee data into SQLite database.
    """

    dataframe.to_sql(
        "employees",
        connection,
        if_exists="replace",
        index=False
    )

    print("Employee data loaded successfully.")

def fetch_employee_data(connection):
    """
    Fetch employee data from SQLite database.
    """

    query = "SELECT * FROM employees"

    dataframe = pd.read_sql(
        query,
        connection
    )

    return dataframe