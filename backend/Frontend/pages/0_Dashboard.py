import streamlit as st

# --- AUTH CHECK ---
if not st.session_state.get("logged_in"):
    st.warning("⚠️ Please login first")
    st.switch_page("home.py")

st.set_page_config(page_title="Dashboard", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
    margin-top: 30px;
}

.card {
    background: linear-gradient(135deg, #eef2ff, #ffffff);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 14px 30px rgba(0,0,0,0.15);
}

.icon {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    background: #4f46e5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    color: white;
    margin: auto;
    margin-bottom: 15px;
}

.card-title {
    font-size: 17px;
    font-weight: 600;
    color: #1f2937;
}
</style>
""", unsafe_allow_html=True)

# --- PAGE TITLE ---
st.markdown("## 📊 Child Vaccination Dashboard")
st.markdown("Select a module to continue")

# --- CARD GRID ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

def dashboard_card(icon, title, page):
    if st.button(title, key=title):
        st.switch_page(page)

    st.markdown(f"""
    <div class="card">
        <div class="icon">{icon}</div>
        <div class="card-title">{title}</div>
    </div>
    """, unsafe_allow_html=True)

# --- ROW 1 ---
dashboard_card("👶", "Child Profile", "pages/3_Child_Profile.py")
dashboard_card("💉", "Vaccination Tracker", "pages/4_Vaccination_Tracker.py")
dashboard_card("📅", "Vaccination Schedule", "pages/5_Vaccination_Schedule.py")

# --- ROW 2 ---
dashboard_card("⚠️", "Risk Prediction", "pages/6_Risk_Prediction.py")
dashboard_card("🩺", "Doctor Notes", "pages/8_Doctor_Notes.py")
dashboard_card("📜", "Vaccination History", "pages/14_Vaccination_History.py")

# --- ROW 3 ---
dashboard_card("⏰", "Reminders", "pages/10_Reminders.py")
dashboard_card("🔔", "Notifications", "pages/11_Notifications.py")
dashboard_card("⚙️", "Profile Settings", "pages/15_Profile_Settings.py")

st.markdown('</div>', unsafe_allow_html=True)
