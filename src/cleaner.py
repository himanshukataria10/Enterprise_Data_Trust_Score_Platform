"""
Module : cleaner.py

Purpose:
Clean employee dataset.
"""

import pandas as pd


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def fill_missing_values(df):
    """Fill missing values."""

    if "Salary" in df.columns:
        df["Salary"] = df["Salary"].fillna(df["Salary"].median())

    if "Department" in df.columns:
        df["Department"] = df["Department"].fillna("Unknown")

    return df


def fix_invalid_salary(df):
    """Replace negative salary with median salary."""

    median_salary = df[df["Salary"] > 0]["Salary"].median()

    df.loc[df["Salary"] <= 0, "Salary"] = median_salary

    return df


def clean_data(df):
    """Complete cleaning pipeline."""

    df = remove_duplicates(df)
    df = fill_missing_values(df)
    df = fix_invalid_salary(df)

    return df