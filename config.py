"""
Enterprise Data Trust Score Platform

Module: config.py

Purpose:
Store all project configuration settings.
"""

import os

# -------------------------------------------------
# Project Root
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------------------------
# Data Paths
# -------------------------------------------------

DATA_FOLDER = os.path.join(BASE_DIR, "data")

RAW_DATA_PATH = os.path.join(
    DATA_FOLDER,
    "raw",
    "employee_data.csv"
)

DIRTY_DATA_PATH = os.path.join(
    DATA_FOLDER,
    "processed",
    "dirty_employee_data.csv"
)

CLEAN_DATA_PATH = os.path.join(
    DATA_FOLDER,
    "processed",
    "clean_employee_data.csv"
)

# -------------------------------------------------
# Output Paths
# -------------------------------------------------

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "outputs"
)

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "images"
)

REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "reports"
)

# -------------------------------------------------
# Database
# -------------------------------------------------

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "database",
    "enterprise_data.db"
)

# -------------------------------------------------
# Logs
# -------------------------------------------------

LOG_FOLDER = os.path.join(
    BASE_DIR,
    "logs"
)

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "pipeline.log"
)