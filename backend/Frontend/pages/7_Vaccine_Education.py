import streamlit as st

st.set_page_config(page_title="Vaccine Education", layout="wide")

st.title("💉 Vaccine Education for Children")
st.markdown(
    """
    Vaccination protects children from serious and life-threatening diseases.
    Giving vaccines at the **right age and right time** is crucial for building
    strong immunity and preventing outbreaks.
    """
)

st.divider()

# ---------------- BCG ----------------
st.subheader("🩺 BCG (Bacillus Calmette–Guérin)")

st.markdown("""
**Disease Prevented:** Tuberculosis (TB)

**Recommended Age:** At birth or within first 4 weeks

**Why is it important?**
- Protects infants from severe forms of TB
- Prevents TB meningitis and widespread TB infection
- Very important in countries like India where TB is common

**If missed or delayed:**
- Higher risk of severe TB
- Possible brain infection (TB meningitis)
""")

st.divider()

# ---------------- OPV ----------------
st.subheader("🧃 OPV (Oral Polio Vaccine)")

st.markdown("""
**Disease Prevented:** Poliomyelitis (Polio)

**Recommended Age:**
- At birth
- 6 weeks
- 10 weeks
- 14 weeks

**Why is it important?**
- Prevents permanent paralysis
- Easy oral administration
- Helps stop spread of polio in the community

**If missed or delayed:**
- Risk of lifelong paralysis
- Increased outbreak risk
""")

st.divider()

# ---------------- IPV ----------------
st.subheader("💉 IPV (Inactivated Polio Vaccine)")

st.markdown("""
**Disease Prevented:** Polio

**Recommended Age:**
- 6 weeks
- 14 weeks

**Why is it important?**
- Provides strong individual immunity
- No risk of vaccine-derived polio
- Complements OPV for complete protection

**If missed or delayed:**
- Lower immunity against polio
""")

st.divider()

# ---------------- DPT ----------------
st.subheader("🧬 DPT (Diphtheria, Pertussis, Tetanus)")

st.markdown("""
**Diseases Prevented:**
- Diphtheria
- Pertussis (Whooping Cough)
- Tetanus

**Recommended Age:**
- 6 weeks
- 10 weeks
- 14 weeks
- Booster at 16–24 months

**Why is it important?**
- Protects against breathing problems and severe cough
- Prevents tetanus infections
- Reduces child mortality

**If missed or delayed:**
- Risk of respiratory failure
- Tetanus can be fatal
""")

st.divider()

# ---------------- Hepatitis B ----------------
st.subheader("🧪 Hepatitis B Vaccine")

st.markdown("""
**Disease Prevented:** Hepatitis B (Liver Infection)

**Recommended Age:**
- At birth (within 24 hours)
- 6 weeks
- 10 weeks
- 14 weeks

**Why is it important?**
- Prevents chronic liver disease
- Reduces risk of liver cancer
- Prevents mother-to-child transmission

**If missed or delayed:**
- Lifelong liver infection risk
""")

st.divider()

# ---------------- MMR ----------------
st.subheader("🧠 MMR (Measles, Mumps, Rubella)")

st.markdown("""
**Diseases Prevented:**
- Measles
- Mumps
- Rubella

**Recommended Age:**
- 9 months
- Booster at 15–18 months

**Why is it important?**
- Prevents outbreaks
- Protects against brain damage and pneumonia
- Prevents birth defects caused by rubella

**If missed or delayed:**
- High risk of epidemics
- Severe long-term complications
""")

st.divider()

# ---------------- Importance ----------------
st.subheader("📌 Why Timely Vaccination Matters")

st.markdown("""
- Builds immunity at the right developmental stage
- Protects infants when they are most vulnerable
- Helps achieve herd immunity
- Prevents disability and death
""")

st.success("✅ Timely vaccination saves lives and ensures a healthy future for children.")
