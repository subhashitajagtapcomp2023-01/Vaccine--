import streamlit as st
import pandas as pd
import os
from datetime import datetime

if "child_id" not in st.session_state:
    st.warning("Login required")
    st.stop()

child_id = st.session_state["child_id"]

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "data", "7_notifications.csv")

st.title("🔔 Notifications")

if os.path.exists(PATH):
    df = pd.read_csv(PATH)
else:
    df = pd.DataFrame(columns=["child_id", "message", "date"])

msgs = df[df["child_id"] == child_id]

if msgs.empty:
    st.info("No notifications yet")
else:
    for _, row in msgs.iterrows():
        st.success(f"{row['date']} — {row['message']}")
