import streamlit as st
from datetime import date

# --- AUTH CHECK ---
if not st.session_state.get("logged_in"):
    st.warning("⚠️ Please login first")
    st.switch_page("home.py")

st.set_page_config(page_title="Vaccination History", layout="wide")

# --- PAGE HEADER ---
st.markdown("## 📖 Vaccination History Timeline")
st.markdown("### 👶 Child: Isha (C0310)")

# --- SAMPLE DATA (DEMO PURPOSE) ---
vaccination_history = [
    {
        "vaccine": "BCG",
        "age": "At Birth",
        "date": "2023-06-01",
        "doctor": "Dr. Mehta",
        "hospital": "City Government Hospital",
        "status": "Completed"
    },
    {
        "vaccine": "Hepatitis B (1st Dose)",
        "age": "6 Weeks",
        "date": "2023-07-15",
        "doctor": "Dr. Sharma",
        "hospital": "City Government Hospital",
        "status": "Completed"
    },
    {
        "vaccine": "DTP (1st Dose)",
        "age": "10 Weeks",
        "date": "2023-08-10",
        "doctor": "Dr. Sharma",
        "hospital": "City Government Hospital",
        "status": "Completed"
    },
    {
        "vaccine": "Polio Booster",
        "age": "14 Weeks",
        "date": "2023-09-05",
        "doctor": "Dr. Rao",
        "hospital": "Primary Health Center",
        "status": "Completed"
    },
    {
        "vaccine": "Measles",
        "age": "9 Months",
        "date": "Upcoming",
        "doctor": "-",
        "hospital": "-",
        "status": "Upcoming"
    }
]

# --- STYLING ---
st.markdown("""
<style>
.timeline-card {
    background: #f8fafc;
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 18px;
    border-left: 6px solid #4f46e5;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}

.completed {
    border-left-color: #22c55e;
}

.upcoming {
    border-left-color: #f59e0b;
}

.vaccine-name {
    font-size: 18px;
    font-weight: 600;
}

.meta {
    color: #555;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --- DISPLAY TIMELINE ---
for v in vaccination_history:
    status_class = "completed" if v["status"] == "Completed" else "upcoming"
    status_icon = "✅" if v["status"] == "Completed" else "⏳"

    st.markdown(f"""
    <div class="timeline-card {status_class}">
        <div class="vaccine-name">{status_icon} {v["vaccine"]}</div>
        <div class="meta">🗓 Age: {v["age"]}</div>
        <div class="meta">📅 Date: {v["date"]}</div>
        <div class="meta">👨‍⚕️ Doctor: {v["doctor"]}</div>
        <div class="meta">🏥 Hospital: {v["hospital"]}</div>
    </div>
    """, unsafe_allow_html=True)
