import streamlit as st
import pandas as pd
import os

st.title("⚠️ Health Risk Prediction")

if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

CSV_PATH = os.path.join(DATA_DIR, "backend_children.csv")
df = pd.read_csv(CSV_PATH)

child = df[df["child_id"] == st.session_state["child_id"]]

if child.empty:
    st.error("Child data not found")
else:
    pending = child.iloc[0]["pending_vaccines"]
    age = child.iloc[0]["child_age_years"]

    if pd.isna(pending) or pending == "None":
        risk = "LOW"
        msg = "Child is fully vaccinated."
    elif age < 2:
        risk = "HIGH"
        msg = "Critical vaccines pending at early age."
    else:
        risk = "MEDIUM"
        msg = "Vaccines pending — schedule follow-up."

    st.metric("Predicted Risk Level", risk)
    st.info(msg)
