import pandas as pd

FILE_PATH = "data/processed/realtime_data.parquet"

def write_data(data):
    df = pd.DataFrame(data)
    df.to_parquet(FILE_PATH, index=False)