import streamlit as st

st.title("⚙️ Profile Settings")

st.subheader("🔐 Security")

new_password = st.text_input("Change Password", type="password")

if st.button("Update Password"):
    st.success("Password updated successfully")

st.divider()

st.subheader("👤 Preferences")

notif = st.checkbox("Enable Notifications", value=True)
dark = st.checkbox("Dark Mode")

st.success("Settings saved")
