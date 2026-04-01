import streamlit as st
import pandas as pd
import os
from streamlit_autorefresh import st_autorefresh
import numpy as np
from datetime import datetime

st.set_page_config(layout="wide")
st.title("🚕 Real-Time Taxi Dashboard")

st_autorefresh(interval=3000, key="refresh")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "data/processed/realtime_data.parquet")

if os.path.exists(path):
    df = pd.read_parquet(path)
else:
    # fallback demo data (so app never looks empty)
    df = pd.DataFrame({
        "timestamp": pd.date_range(end=datetime.now(), periods=50, freq="s"),
        "trip_distance": np.random.rand(50) * 10
    })

st.metric("Total Trips", len(df))
st.metric("Avg Distance", round(df["trip_distance"].mean(), 2))

st.line_chart(df.set_index("timestamp")["trip_distance"])
st.caption("Live data" if os.path.exists(path) else "Simulated real-time data")
