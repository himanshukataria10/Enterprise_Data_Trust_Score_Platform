"""
Module : trust_score.py

Purpose:
Calculate employee Trust Score.
"""

import pandas as pd


VALID_DEPARTMENTS = [
    "HR",
    "IT",
    "Finance",
    "Sales",
    "Marketing",
    "Operations"
]


def calculate_trust_score(row):
    score = 100

    # Invalid Salary
    if row["Salary"] <= 0:
        score -= 20

    # Invalid Department
    if row["Department"] not in VALID_DEPARTMENTS:
        score -= 15

    # Future Joining Date
    joining_date = pd.to_datetime(row["Joining_Date"])

    if joining_date > pd.Timestamp.today():
        score -= 15

    return max(score, 0)


def assign_category(score):

    if score >= 90:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Poor"