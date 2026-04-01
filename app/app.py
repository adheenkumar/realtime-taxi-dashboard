import streamlit as st
import pandas as pd
import os
from streamlit_autorefresh import st_autorefresh

st.set_page_config(layout="wide")
st.title("🚕 Real-Time Taxi Dashboard")

st_autorefresh(interval=3000, key="refresh")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "data/processed/realtime_data.parquet")

if os.path.exists(path):
    df = pd.read_parquet(path)

    st.metric("Total Trips", len(df))
    st.metric("Avg Distance", round(df["trip_distance"].mean(), 2))

    st.line_chart(df.set_index("timestamp")["trip_distance"])
else:
    st.warning("Waiting for data...")
