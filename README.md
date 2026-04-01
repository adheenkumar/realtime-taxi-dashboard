# 🚕 Real-Time Taxi Analytics Dashboard

## 📌 Overview

This project simulates a **near real-time data engineering pipeline** for taxi trip analytics. It demonstrates how streaming-like data can be ingested, processed, and visualized using a lightweight architecture.

The system generates realistic taxi trip data (including peak-hour patterns and anomalies), stores it in a data lake (Parquet), and visualizes key metrics via a Streamlit dashboard.

---

## 🏗️ Architecture

```
Data Simulator → Parquet (Data Lake) → Streamlit Dashboard
```

* **Producer**: Python-based simulator (streaming-like data generation)
* **Storage**: Parquet files (data lake pattern)
* **Consumer**: Streamlit dashboard (real-time visualization)

---

## ⚙️ Features

### 🚀 Real-Time Simulation

* Generates continuous taxi trip data
* Simulates:

  * Peak hours (morning/evening)
  * Traffic bursts
  * Anomalies (spikes in trip distance)

### 📊 Dashboard (Streamlit)

* Auto-refresh every few seconds
* Interactive time window selection (1, 5, 15 minutes)
* Metrics:

  * Total trips
  * Average distance
  * Rolling window average
  * Rolling window max
  * Trips per second (throughput)
* Trend indicators (delta vs previous window)

### 🧠 Analytics Concepts

* Event-time processing
* Sliding window aggregations
* Near real-time monitoring

---

## 📂 Project Structure

```
realtime-taxi-dashboard/
│
├── app/
│   └── app.py                # Streamlit dashboard
│
├── pipeline/
│   └── data_simulator.py     # Real-time data generator
│
├── data/
│   └── processed/            # Parquet output
│
├── tests/
│
├── requirements.txt
└── run_pipeline.sh
```

---

## ▶️ How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start data simulator

```bash
python pipeline/data_simulator.py
```

### 3. Run dashboard

```bash
streamlit run app/app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

* Deploy only the Streamlit app
* Simulator does NOT run in cloud

### Behavior:

* If parquet exists → uses real data
* Else → falls back to simulated data

---

## 📈 Key Metrics Explained

* **Rolling Avg (N min)**: Average trip distance over selected time window
* **Rolling Max (N min)**: Maximum trip distance in window
* **Throughput (Trips/sec)**: Number of trips processed per second
* **Delta**: Change compared to previous time window

---

## 🧪 Future Improvements

* Kafka-based streaming ingestion
* Spark Structured Streaming for processing
* API-based data serving (FastAPI)
* Persistent storage (PostgreSQL / Delta Lake)
* Advanced anomaly detection

---

## 💼 Resume Value

This project demonstrates:

* Real-time data pipeline design
* Streaming simulation techniques
* Time-windowed aggregations
* Dashboarding and monitoring
* Cloud deployment and debugging

---

## 📌 Tech Stack

* Python
* Pandas
* Streamlit
* NumPy
* Parquet (PyArrow)

---

## 📷 Demo

https://realtime-taxi-dashboard-sbrj3dghxnuezyof72wwcy.streamlit.app/

---

## 👤 Author

Dheenkumar
