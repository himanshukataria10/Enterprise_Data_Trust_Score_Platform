"""
Enterprise Data Trust Score Platform

Module: visualization.py

Purpose:
Generate and save project visualizations.
"""

import os
import matplotlib.pyplot as plt


def generate_all_visualizations(df):
    """
    Generate all project charts.
    """

    os.makedirs("images", exist_ok=True)

    # -----------------------------------------
    # Salary Distribution
    # -----------------------------------------

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Salary"],
        bins=10
    )

    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Employees")

    plt.tight_layout()

    plt.savefig(
        "images/salary_distribution.png",
        dpi=300
    )

    plt.close()

    # -----------------------------------------
    # Department Distribution
    # -----------------------------------------

    plt.figure(figsize=(8, 5))

    df["Department"].value_counts().plot(
        kind="bar"
    )

    plt.title("Department Distribution")
    plt.xlabel("Department")
    plt.ylabel("Employees")

    plt.tight_layout()

    plt.savefig(
        "images/department_distribution.png",
        dpi=300
    )

    plt.close()

    # -----------------------------------------
    # Trust Category Distribution
    # -----------------------------------------

    plt.figure(figsize=(6, 6))

    df["Trust_Category"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")

    plt.title("Trust Category Distribution")

    plt.tight_layout()

    plt.savefig(
        "images/trust_category_distribution.png",
        dpi=300
    )

    plt.close()

    # -----------------------------------------
    # Trust Score Distribution
    # -----------------------------------------

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Trust_Score"],
        bins=10
    )

    plt.title("Trust Score Distribution")
    plt.xlabel("Trust Score")
    plt.ylabel("Employees")

    plt.tight_layout()

    plt.savefig(
        "images/trust_score_distribution.png",
        dpi=300
    )

    plt.close()

    # -----------------------------------------
    # City Distribution
    # -----------------------------------------

    plt.figure(figsize=(8, 5))

    df["City"].value_counts().plot(
        kind="bar"
    )

    plt.title("City Distribution")
    plt.xlabel("City")
    plt.ylabel("Employees")

    plt.tight_layout()

    plt.savefig(
        "images/city_distribution.png",
        dpi=300
    )

    plt.close()

    print("✓ All visualizations generated successfully.")