import time
from datetime import datetime
from writer import write_data
import random

def generate_row():
    return {
        "timestamp": datetime.now(),
        "trip_distance": round(random.uniform(1, 15), 2),
        "fare_amount": round(random.uniform(5, 50), 2)
    }

data = []

while True:
    data.append(generate_row())
    write_data(data)
    print(f"Generated {len(data)} rows")
    time.sleep(2)