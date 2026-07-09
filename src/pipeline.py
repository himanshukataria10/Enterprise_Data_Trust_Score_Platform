"""
Enterprise Data Trust Score Platform

Module: pipeline.py

Purpose:
Run the complete ETL pipeline.
"""

import os
import pandas as pd

from cleaner import clean_data

from trust_score import (
    calculate_trust_score,
    assign_category
)

from database import (
    create_connection,
    create_employee_table,
    load_employee_data,
    fetch_employee_data
)

from logger import logger
from visualization import generate_all_visualizations


def run_pipeline():
    """
    Execute the complete ETL pipeline.
    """

    logger.info("Pipeline Started")

    print("=" * 60)
    print("Enterprise Data Trust Score Platform")
    print("=" * 60)

    # -------------------------------------------------
    # Create Output Folder
    # -------------------------------------------------

    os.makedirs("outputs", exist_ok=True)
    os.makedirs("images", exist_ok=True)

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    print("\n[1] Loading Dataset...")

    clean_df = pd.read_csv(
        "data/processed/clean_employee_data.csv"
    )

    logger.info("Dataset Loaded Successfully")
    print("✓ Dataset Loaded Successfully")

    # -------------------------------------------------
    # Data Cleaning
    # -------------------------------------------------

    print("\n[2] Cleaning Dataset...")

    clean_df = clean_data(clean_df)

    logger.info("Data Cleaning Completed")
    print("✓ Data Cleaning Completed")

    # -------------------------------------------------
    # Trust Score
    # -------------------------------------------------

    print("\n[3] Calculating Trust Score...")

    clean_df["Trust_Score"] = clean_df.apply(
        calculate_trust_score,
        axis=1
    )

    clean_df["Trust_Category"] = clean_df["Trust_Score"].apply(
        assign_category
    )

    logger.info("Trust Score Generated")
    print("✓ Trust Score Generated")

    # -------------------------------------------------
    # Save Clean Dataset
    # -------------------------------------------------

    clean_df.to_csv(
        "data/processed/clean_employee_data.csv",
        index=False
    )

    logger.info("Clean Dataset Saved")
    print("✓ Clean Dataset Saved")

    # -------------------------------------------------
    # Database
    # -------------------------------------------------

    print("\n[4] Connecting Database...")

    connection = create_connection()

    create_employee_table(connection)

    logger.info("Database Connected")
    print("✓ Database Connected")

    load_employee_data(
        connection,
        clean_df
    )

    logger.info("Employee Data Loaded Into Database")
    print("✓ Employee Data Loaded Into Database")

    # -------------------------------------------------
    # Fetch Data
    # -------------------------------------------------

    database_df = fetch_employee_data(connection)

    logger.info("Database Data Retrieved")

    print("\nFirst Five Records\n")
    print(database_df.head())

    # -------------------------------------------------
    # Generate Visualizations
    # -------------------------------------------------

    print("\n[5] Generating Visualizations...")

    generate_all_visualizations(database_df)

    logger.info("Visualizations Generated")
    print("✓ Visualizations Generated")

    # -------------------------------------------------
    # Employee Summary
    # -------------------------------------------------

    employee_summary = database_df[
        [
            "Employee_ID",
            "Department",
            "Salary",
            "Trust_Score",
            "Trust_Category"
        ]
    ]

    employee_summary.to_csv(
        "outputs/employee_summary.csv",
        index=False
    )

    logger.info("Employee Summary Generated")
    print("✓ Employee Summary Generated")

    # -------------------------------------------------
    # Department Summary
    # -------------------------------------------------

    department_summary = (
        database_df
        .groupby("Department")
        .agg(
            Total_Employees=("Employee_ID", "count"),
            Average_Salary=("Salary", "mean"),
            Average_Trust_Score=("Trust_Score", "mean")
        )
        .reset_index()
    )

    department_summary.to_csv(
        "outputs/department_summary.csv",
        index=False
    )

    logger.info("Department Summary Generated")
    print("✓ Department Summary Generated")

    # -------------------------------------------------
    # Trust Category Summary
    # -------------------------------------------------

    trust_summary = (
        database_df["Trust_Category"]
        .value_counts()
        .reset_index()
    )

    trust_summary.columns = [
        "Trust_Category",
        "Total_Employees"
    ]

    trust_summary.to_csv(
        "outputs/trust_summary.csv",
        index=False
    )

    logger.info("Trust Summary Generated")
    print("✓ Trust Summary Generated")

    # -------------------------------------------------
    # Pipeline Summary
    # -------------------------------------------------

    summary_df = pd.DataFrame({
        "Metric": [
            "Total Employees",
            "Departments",
            "Average Salary",
            "Average Trust Score",
            "Highest Salary",
            "Lowest Salary"
        ],
        "Value": [
            len(database_df),
            database_df["Department"].nunique(),
            round(database_df["Salary"].mean(), 2),
            round(database_df["Trust_Score"].mean(), 2),
            round(database_df["Salary"].max(), 2),
            round(database_df["Salary"].min(), 2)
        ]
    })

    summary_df.to_csv(
        "outputs/pipeline_summary.csv",
        index=False
    )

    logger.info("Pipeline Summary Generated")
    print("✓ Pipeline Summary Generated")

    # -------------------------------------------------
    # Console Summary
    # -------------------------------------------------

    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY")
    print("=" * 60)

    print(f"Total Employees      : {len(database_df)}")
    print(f"Departments          : {database_df['Department'].nunique()}")
    print(f"Average Salary       : {database_df['Salary'].mean():,.2f}")
    print(f"Average Trust Score  : {database_df['Trust_Score'].mean():.2f}")
    print(f"Highest Salary       : {database_df['Salary'].max():,.2f}")
    print(f"Lowest Salary        : {database_df['Salary'].min():,.2f}")

    print("=" * 60)

    connection.close()

    logger.info("Database Connection Closed")
    logger.info("Pipeline Completed Successfully")

    print("\n✓ Database Connection Closed")
    print("✓ Pipeline Completed Successfully")