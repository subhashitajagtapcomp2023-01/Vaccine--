import streamlit as st
import pandas as pd
import os
from datetime import date

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")

CHILDREN_CSV = os.path.join(DATA_DIR, "backend_children.csv")
SCHEDULE_CSV = os.path.join(DATA_DIR, "4_vaccination_schedule.csv")
MASTER_CSV = os.path.join(DATA_DIR, "3_vaccination_master.csv")

st.title("📅 Vaccination Schedule")

# ---------------- LOGIN CHECK ----------------
if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

child_id = st.session_state["child_id"]

# ---------------- LOAD CHILD ----------------
if not os.path.exists(CHILDREN_CSV):
    st.error("Child data file missing")
    st.stop()

df_children = pd.read_csv(CHILDREN_CSV)
child = df_children[df_children["child_id"] == child_id]

if child.empty:
    st.error("Child not found")
    st.stop()

child = child.iloc[0]

# ---------------- DISPLAY CHILD ----------------
st.subheader("👶 Child Details")
st.write(f"**Name:** {child.get('child_name', 'N/A')}")
st.write(f"**Child ID:** {child_id}")

# ---------------- LOAD VACCINES ----------------
vaccine_list = []

if os.path.exists(MASTER_CSV):
    df_master = pd.read_csv(MASTER_CSV)
    if "vaccine_name" in df_master.columns:
        vaccine_list = df_master["vaccine_name"].dropna().unique().tolist()

vaccine_list.append("Other")

# ---------------- SCHEDULE FORM ----------------
st.subheader("📝 Schedule a Vaccination")

with st.form("schedule_form"):
    vaccine = st.selectbox("Select Vaccine", vaccine_list)

    custom_vaccine = ""
    if vaccine == "Other":
        custom_vaccine = st.text_input("Enter Vaccine Name")

    schedule_date = st.date_input("Vaccination Date", min_value=date.today())
    location = st.text_input("Location (Hospital / PHC / Anganwadi)")
    notes = st.text_area("Additional Notes (optional)")

    submitted = st.form_submit_button("✅ Save Schedule")

# ---------------- SAVE DATA ----------------
if submitted:
    final_vaccine = custom_vaccine if vaccine == "Other" else vaccine

    if not final_vaccine or not location:
        st.error("Please fill all required fields")
    else:
        new_row = {
            "child_id": child_id,
            "child_name": child.get("child_name", ""),
            "vaccine_name": final_vaccine,
            "scheduled_date": schedule_date,
            "location": location,
            "notes": notes
        }

        if os.path.exists(SCHEDULE_CSV):
            df_sched = pd.read_csv(SCHEDULE_CSV)
            df_sched = pd.concat([df_sched, pd.DataFrame([new_row])], ignore_index=True)
        else:
            df_sched = pd.DataFrame([new_row])

        df_sched.to_csv(SCHEDULE_CSV, index=False)

        st.success("🎉 Vaccination scheduled successfully!")

# ---------------- SHOW UPCOMING ----------------
st.subheader("📌 Upcoming Vaccinations")

if os.path.exists(SCHEDULE_CSV):
    df_sched = pd.read_csv(SCHEDULE_CSV)
    child_sched = df_sched[df_sched["child_id"] == child_id]

    if child_sched.empty:
        st.info("No scheduled vaccinations yet.")
    else:
        st.dataframe(child_sched)
