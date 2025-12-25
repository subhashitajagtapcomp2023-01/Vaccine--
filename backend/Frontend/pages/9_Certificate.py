import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Vaccination Certificate", layout="centered")
st.title("📜 Vaccination Certificate")

st.write(
    "Generate an official **Vaccination Certificate (PDF)** "
    "for registered children."
)

# ---------------- CORRECT PATH ----------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "backend_children.csv")

# ---------------- LOAD DATA ----------------
if not os.path.exists(DATA_PATH):
    st.error(f"❌ Data file not found at:\n{DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

if df.empty:
    st.warning("⚠️ No child records found.")
    st.stop()

# ---------------- SAFE COLUMNS ----------------
required_cols = ["child_name", "dob", "gender", "parent_name", "vaccination_status"]
for col in required_cols:
    if col not in df.columns:
        df[col] = "Not Available"

# ---------------- SELECT CHILD ----------------
st.subheader("👶 Select Child")

child_name = st.selectbox("Child Name", df["child_name"].unique())
child = df[df["child_name"] == child_name].iloc[0]

# ---------------- PDF GENERATOR ----------------
def generate_pdf(child):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 80, "Vaccination Certificate")

    c.setFont("Helvetica", 12)
    y = height - 150

    details = [
        f"Child Name: {child['child_name']}",
        f"Date of Birth: {child['dob']}",
        f"Gender: {child['gender']}",
        f"Parent / Guardian: {child['parent_name']}",
        "",
        "Vaccination Status:",
        f"{child['vaccination_status']}",
        "",
        f"Issue Date: {datetime.now().strftime('%d %B %Y')}",
        "",
        "Authorized By:",
        "Digital Health Immunization System"
    ]

    for line in details:
        c.drawString(80, y, line)
        y -= 22

    c.rect(60, 100, width - 120, height - 220)
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

# ---------------- PREVIEW ----------------
st.subheader("📄 Certificate Details")

st.markdown(f"""
**Child Name:** {child['child_name']}  
**DOB:** {child['dob']}  
**Gender:** {child['gender']}  
**Parent:** {child['parent_name']}  
**Vaccination Status:** {child['vaccination_status']}
""")

# ---------------- DOWNLOAD ----------------
pdf_file = generate_pdf(child)

st.download_button(
    label="⬇️ Download PDF Certificate",
    data=pdf_file,
    file_name=f"{child_name}_Vaccination_Certificate.pdf",
    mime="application/pdf"
)

st.success("✅ PDF certificate generated successfully")
