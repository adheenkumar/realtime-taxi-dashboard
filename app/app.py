import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(layout="wide")
st.title("🚕 Real-Time Taxi Dashboard")

# Auto-refresh every 3 seconds
st_autorefresh(interval=3000, key="refresh")

# -------------------------------
# File Path Handling
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "data/processed/realtime_data.parquet")

# -------------------------------
# Load or Simulate Data
# -------------------------------
if os.path.exists(path):
    df = pd.read_parquet(path)
    st.caption("📡 Live data")
else:
    # Simulated real-time data
    df = pd.DataFrame({
        "timestamp": pd.date_range(end=datetime.now(), periods=50, freq="s"),
        "trip_distance": np.random.rand(50) * 10
    })
    st.caption("⚠️ Simulated real-time data")

# -------------------------------
# Data Preparation
# -------------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# -------------------------------
# Rolling Window (Last 5 Minutes)
# -------------------------------
now = df["timestamp"].max()
window_start = now - timedelta(minutes=5)

df_5min = df[df["timestamp"] >= window_start]

# -------------------------------
# Metrics
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trips", len(df))
col2.metric("Avg Distance", round(df["trip_distance"].mean(), 2))
col3.metric("5-min Avg Distance", round(df_5min["trip_distance"].mean(), 2))
col4.metric("5-min Max Distance", round(df_5min["trip_distance"].max(), 2))

# -------------------------------
# Chart
# -------------------------------
st.subheader("Trip Distance Over Time")
st.line_chart(df.set_index("timestamp")["trip_distance"])
