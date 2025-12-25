import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("📝 Doctor Notes")

# ---------------- LOGIN CHECK ----------------
if "child_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

child_id = st.session_state["child_id"]

# ---------------- PATH SETUP (CORRECT) ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

NOTES_CSV = os.path.join(DATA_DIR, "6_doctor_notes.csv")

# ---------------- LOAD EXISTING NOTES ----------------
if os.path.exists(NOTES_CSV):
    df_notes = pd.read_csv(NOTES_CSV)
else:
    df_notes = pd.DataFrame(
        columns=["child_id", "note", "created_at"]
    )

# ---------------- NOTE INPUT ----------------
note_text = st.text_area(
    "Enter doctor's note or advice",
    height=120,
    placeholder="E.g. Child has mild fever, give paracetamol if needed"
)

if st.button("💾 Save Note"):
    if note_text.strip() == "":
        st.error("Note cannot be empty")
    else:
        new_note = {
            "child_id": child_id,
            "note": note_text,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        df_notes = pd.concat(
            [df_notes, pd.DataFrame([new_note])],
            ignore_index=True
        )

        df_notes.to_csv(NOTES_CSV, index=False)
        st.success("Doctor note saved successfully!")

# ---------------- SHOW PREVIOUS NOTES ----------------
st.subheader("📋 Previous Notes")

child_notes = df_notes[df_notes["child_id"] == child_id]

if child_notes.empty:
    st.info("No doctor notes available yet.")
else:
    for _, row in child_notes.sort_values("created_at", ascending=False).iterrows():
        st.markdown(
            f"""
            **🗓 {row['created_at']}**  
            {row['note']}
            ---
            """
        )
