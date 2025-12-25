import streamlit as st
import pandas as pd
import os

st.title("💉 Vaccination Tracker")

if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

CSV_PATH = os.path.join(DATA_DIR, "backend_children.csv")
df = pd.read_csv(CSV_PATH)

child_id = st.session_state["child_id"]
child = df[df["child_id"] == child_id]

if child.empty:
    st.error("Child record not found")
else:
    st.subheader("Vaccination Status")
    st.dataframe(
        child[[
            "completed_vaccine",
            "vaccination_status",
            "pending_vaccines",
            "upcoming_vaccination_name",
            "upcoming_vaccination_date"
        ]]
    )
