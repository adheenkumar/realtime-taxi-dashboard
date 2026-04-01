# pipeline/utils.py

import random
from datetime import datetime


def generate_timestamp():
    """Generate current timestamp"""
    return datetime.now()


def generate_trip_distance(min_val=1.0, max_val=15.0):
    """Generate realistic trip distance"""
    return round(random.uniform(min_val, max_val), 2)


def generate_fare_amount(min_val=5.0, max_val=50.0):
    """Generate realistic fare amount"""
    return round(random.uniform(min_val, max_val), 2)


def generate_row():
    """Generate a single taxi trip record"""
    return {
        "timestamp": generate_timestamp(),
        "trip_distance": generate_trip_distance(),
        "fare_amount": generate_fare_amount()
    }


# ----------------------------
# Data Quality Checks
# ----------------------------

def validate_row(row):
    """Basic row-level validation"""
    if row["trip_distance"] < 0:
        return False

    if row["fare_amount"] < 0:
        return False

    if not isinstance(row["timestamp"], datetime):
        return False

    return True


def validate_batch(data):
    """Validate list of records"""
    return all(validate_row(row) for row in data)