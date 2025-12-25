import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Vaccine-संस्कार",
    page_icon="🩺",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f8fbff;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: #0b5394;
}

.tagline {
    font-size: 22px;
    color: #38761d;
    margin-top: -10px;
}

.info-text {
    font-size: 18px;
    color: #444;
    line-height: 1.6;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 12px 35px rgba(0,0,0,0.15);
}

.card-title {
    font-size: 22px;
    font-weight: 700;
    color: #0b5394;
    margin-top: 15px;
}

.card-desc {
    font-size: 16px;
    color: #555;
    margin-top: 8px;
}

.card-btn {
    margin-top: 20px;
    width: 100%;
    border-radius: 10px;
}

.footer {
    margin-top: 60px;
    text-align: center;
    color: #777;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown('<div class="hero-title">🩺 Vaccine-संस्कार</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Every dose, a promise of protection</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-text">
    Vaccine-संस्कार helps mothers track, manage, and understand their child’s 
    vaccination journey from birth onwards.<br><br>

    ✔ Never miss a vaccine<br>
    ✔ Track vaccination history easily<br>
    ✔ Get instant answers from AI assistant<br>
    ✔ Designed specially for Indian mothers
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        "https://s3.ap-south-1.amazonaws.com/assets.klayschools.com/wp-content/uploads/2024/12/20204629/Banner-images-95.webp",
        use_container_width=True
    )

st.markdown("---")

# ---------------- WHY VACCINATION ----------------
st.markdown("## 💉 Why Vaccination is Important?")
st.markdown("""
Vaccination protects children from serious diseases, builds immunity at the right age,
and ensures healthy growth. Timely vaccination is one of the strongest shields
for your child’s future.
""")

st.image(
    "https://prod-cdn.preprod.co-vin.in/assets/images/uwin-images/banner-logo/vaccine-week-banner-box.svg",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- LOGIN & REGISTER CARDS ----------------
col_login, col_register = st.columns(2)

with col_login:
    st.markdown("""
    <div class="card">
        <div style="font-size:60px;">👶</div>
        <div class="card-title">Login</div>
        <div class="card-desc">
            Login using Mother Aadhaar & Child ID
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Go to Login", key="login_btn"):
        st.switch_page("/Users/subhashitajagtap/Desktop/gdghackathon-techxplorers/backend/Frontend/pages/1_Login.py")

with col_register:
    st.markdown("""
    <div class="card">
        <div style="font-size:60px;">➕</div>
        <div class="card-title">Register Child</div>
        <div class="card-desc">
            New here? Add your baby & start tracking vaccines
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Register Baby", key="register_btn"):
        st.switch_page("/Users/subhashitajagtap/Desktop/gdghackathon-techxplorers/backend/Frontend/pages/2_Add_Baby.py")

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
✔ Government-recommended vaccination schedules <br>
✔ Secure & private child health data <br>
✔ Made for Indian mothers
</div>
""", unsafe_allow_html=True)
