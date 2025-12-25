import streamlit as st
import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

SCHEDULE_CSV = os.path.join(DATA_DIR, "4_vaccination_schedule.csv")

st.title("⏰ Vaccination Reminders")

if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

child_id = st.session_state["child_id"]

if not os.path.exists(SCHEDULE_CSV):
    st.info("No vaccination schedule available yet.")
    st.stop()

df = pd.read_csv(SCHEDULE_CSV)

child_sched = df[df["child_id"] == child_id]

if child_sched.empty:
    st.info("No reminders scheduled for this child.")
    st.stop()

today = datetime.today().date()

for _, row in child_sched.iterrows():
    try:
        due_date = pd.to_datetime(row["scheduled_date"]).date()
        days_left = (due_date - today).days

        if days_left >= 0:
            st.success(f"💉 {row['vaccine_name']} in {days_left} days at {row['location']}")
    except:
        continue
