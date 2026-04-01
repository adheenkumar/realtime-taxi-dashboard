# tests/test_data_quality.py

import pandas as pd
from pipeline.utils import validate_row, validate_batch
from datetime import datetime


def test_valid_row():
    row = {
        "timestamp": datetime.now(),
        "trip_distance": 5.0,
        "fare_amount": 20.0
    }
    assert validate_row(row) is True


def test_negative_distance():
    row = {
        "timestamp": datetime.now(),
        "trip_distance": -5.0,
        "fare_amount": 20.0
    }
    assert validate_row(row) is False


def test_negative_fare():
    row = {
        "timestamp": datetime.now(),
        "trip_distance": 5.0,
        "fare_amount": -10.0
    }
    assert validate_row(row) is False


def test_invalid_timestamp():
    row = {
        "timestamp": "invalid_time",
        "trip_distance": 5.0,
        "fare_amount": 20.0
    }
    assert validate_row(row) is False


def test_validate_batch():
    data = [
        {
            "timestamp": datetime.now(),
            "trip_distance": 3.0,
            "fare_amount": 10.0
        },
        {
            "timestamp": datetime.now(),
            "trip_distance": 7.0,
            "fare_amount": 25.0
        }
    ]

    assert validate_batch(data) is True


def test_invalid_batch():
    data = [
        {
            "timestamp": datetime.now(),
            "trip_distance": 3.0,
            "fare_amount": 10.0
        },
        {
            "timestamp": datetime.now(),
            "trip_distance": -7.0,  # invalid
            "fare_amount": 25.0
        }
    ]

    assert validate_batch(data) is False