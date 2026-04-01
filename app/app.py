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

# Auto-refresh
st_autorefresh(interval=3000, key="refresh")

# -------------------------------
# File Path
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
    df = pd.DataFrame({
        "timestamp": pd.date_range(end=datetime.now(), periods=200, freq="s"),
        "trip_distance": np.random.gamma(2, 2, 200)
    })
    st.caption("⚠️ Simulated real-time data")

# -------------------------------
# Preprocessing
# -------------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

now = df["timestamp"].max()

# -------------------------------
# Time Window Selector
# -------------------------------
window_option = st.selectbox(
    "Select Time Window",
    ["1 min", "5 min", "15 min"],
    index=1
)

minutes_map = {"1 min": 1, "5 min": 5, "15 min": 15}
selected_minutes = minutes_map[window_option]

window_start = now - timedelta(minutes=selected_minutes)
df_window = df[df["timestamp"] >= window_start]

# Previous window (for delta)
prev_window_start = window_start - timedelta(minutes=selected_minutes)
df_prev = df[
    (df["timestamp"] >= prev_window_start) &
    (df["timestamp"] < window_start)
]

# -------------------------------
# Metrics
# -------------------------------
avg_current = df_window["trip_distance"].mean()
max_current = df_window["trip_distance"].max()

avg_prev = df_prev["trip_distance"].mean()
max_prev = df_prev["trip_distance"].max()

trips_per_sec = len(df_window) / (selected_minutes * 60)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Trips", len(df))

col2.metric(
    "Avg Distance",
    round(df["trip_distance"].mean(), 2)
)

col3.metric(
    f"{selected_minutes}-min Avg",
    round(avg_current, 2),
    delta=None if pd.isna(avg_prev) else round(avg_current - avg_prev, 2)
)

col4.metric(
    f"{selected_minutes}-min Max",
    round(max_current, 2),
    delta=None if pd.isna(max_prev) else round(max_current - max_prev, 2)
)

col5.metric(
    "Trips/sec",
    round(trips_per_sec, 2)
)

# -------------------------------
# Chart
# -------------------------------
st.subheader("Trip Distance Over Time")
st.line_chart(df_window.set_index("timestamp")["trip_distance"])
