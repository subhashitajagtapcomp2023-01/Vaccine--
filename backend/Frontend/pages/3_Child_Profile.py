import streamlit as st
import pandas as pd
import os

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHILDREN_CSV = os.path.join(DATA_DIR, "backend_children.csv")

st.title("Child Profile")

# ---------------- AUTH CHECK ----------------
if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

child_id = st.session_state["child_id"]

# ---------------- LOAD DATA ----------------
if not os.path.exists(CHILDREN_CSV):
    st.error("Child data file missing")
    st.stop()

df = pd.read_csv(CHILDREN_CSV)

child = df[df["child_id"] == child_id]

if child.empty:
    st.error("No child record found")
    st.stop()

child = child.iloc[0]

# ---------------- DISPLAY ----------------
st.subheader("Basic Information")

st.write(f"**Child Name:** {child.get('child_name', 'N/A')}")
st.write(f"**Child ID:** {child.get('child_id', 'N/A')}")
st.write(f"**Date of Birth:** {child.get('dob', 'N/A')}")
st.write(f"**Mother Name:** {child.get('mother_name', 'N/A')}")
st.write(f"**Mother Aadhar:** {child.get('mother_aadhar', 'N/A')}")
