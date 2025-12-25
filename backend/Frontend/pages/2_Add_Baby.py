import streamlit as st
import pandas as pd
from datetime import date

st.title("🍼 Register / Add Baby")

mother_aadhaar = st.text_input("Mother Aadhaar Number")
child_id = st.text_input("Child ID")
child_name = st.text_input("Child Name")
dob = st.date_input("Date of Birth", max_value=date.today())
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Register Baby"):
    new_data = {
        "mother_aadhaar_number": mother_aadhaar,
        "child_id": child_id,
        "child_name": child_name,
        "date_of_birth": dob,
        "child_age_years": 0,
        "gender": gender,
        "completed_vaccine": "",
        "vaccination_status": "Partial",
        "pending_vaccine": ""
    }

    df = pd.read_csv("../data/backend_children.csv")
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("../data/backend_children.csv", index=False)

    st.success("✅ Baby Registered Successfully")
    st.switch_page("pages/1_Login.py")
