import streamlit as st
import pandas as pd

st.title("🔐 Login")

mother_aadhaar = st.text_input("Mother Aadhaar Number")
child_id = st.text_input("Child ID")

if st.button("Login"):
    df = pd.read_csv("../data/backend_children.csv")

    match = df[
        (df["mother_aadhaar_number"].astype(str) == mother_aadhaar) &
        (df["child_id"].astype(str) == child_id)
    ]

    if not match.empty:
        st.session_state.logged_in = True
        st.session_state.child_id = child_id
        st.success("✅ Login Successful")
        st.switch_page("pages/0_Dashboard.py")
    else:
        st.error("❌ Invalid Aadhaar Number or Child ID")
