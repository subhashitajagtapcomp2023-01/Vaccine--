import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Vaccination Assistant",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# SAMPLE CHILD DATA (Replace with DB / CSV later)
# --------------------------------------------------
child_data = {
    "child_id": "C0310",
    "name": "Isha",
    "age": 1,
    "vaccinations_taken": [
        "BCG",
        "Hepatitis B",
        "DTP",
        "Polio"
    ],
    "pending_vaccinations": [
        "Measles (MMR)"
    ],
    "last_vaccine": "Polio"
}

# --------------------------------------------------
# VACCINE EDUCATION KNOWLEDGE BASE
# --------------------------------------------------
vaccine_education = {
    "bcg": "BCG vaccine protects children from severe forms of tuberculosis.",
    "polio": "Polio vaccine prevents paralysis caused by poliovirus.",
    "dtp": "DTP vaccine protects against Diphtheria, Tetanus and Pertussis.",
    "hepatitis": "Hepatitis B vaccine protects the liver from Hepatitis B virus.",
    "measles": "Measles vaccine (MMR) protects against Measles, Mumps and Rubella."
}

# --------------------------------------------------
# POST-VACCINATION SYMPTOMS KNOWLEDGE
# --------------------------------------------------
post_vaccine_symptoms = {
    "fever": (
        "Mild fever after vaccination is common and usually lasts 1–2 days.\n"
        "You may give paracetamol syrup as advised by a doctor."
    ),
    "swelling": (
        "Mild swelling or redness at the injection site is normal.\n"
        "Apply a cold compress and avoid massaging the area."
    ),
    "pain": (
        "Pain at the injection site is common.\n"
        "It usually reduces within 1–2 days."
    ),
    "vomiting": (
        "Occasional vomiting may occur.\n"
        "Ensure the child stays hydrated."
    ),
    "allergy": (
        "Severe allergic reactions are rare.\n"
        "If you notice breathing difficulty, facial swelling, or high fever, seek medical help immediately."
    )
}

# --------------------------------------------------
# INTENT DETECTION FUNCTION
# --------------------------------------------------
def detect_intent(question: str) -> str:
    q = question.lower()

    if any(word in q for word in ["taken", "completed", "pending", "next", "due"]):
        return "dataset"

    if any(word in q for word in ["fever", "swelling", "pain", "vomit", "allergy", "rash"]):
        return "post_vaccine"

    if any(word in q for word in ["what is", "why", "when", "age", "importance"]):
        return "education"

    return "general"

# --------------------------------------------------
# RESPONSE GENERATION FUNCTION
# --------------------------------------------------
def generate_response(question: str) -> str:
    intent = detect_intent(question)
    q = question.lower()

    # ---------------- DATASET QUESTIONS ----------------
    if intent == "dataset":
        if "pending" in q or "next" in q or "due" in q:
            return (
                f"🧒 **{child_data['name']}** has the following pending vaccination:\n\n"
                f"👉 {', '.join(child_data['pending_vaccinations'])}"
            )

        if "taken" in q or "completed" in q:
            return (
                f"✅ **Vaccinations completed by {child_data['name']}:**\n\n"
                f"{', '.join(child_data['vaccinations_taken'])}"
            )

    # ---------------- POST-VACCINATION SYMPTOMS ----------------
    if intent == "post_vaccine":
        for symptom, response in post_vaccine_symptoms.items():
            if symptom in q:
                return (
                    f"🩺 {response}\n\n"
                    "⚠️ If symptoms worsen or persist, please consult a doctor."
                )

    # ---------------- EDUCATIONAL QUESTIONS ----------------
    if intent == "education":
        for vaccine, info in vaccine_education.items():
            if vaccine in q:
                return f"💉 **{info}**"

    # ---------------- FALLBACK RESPONSE ----------------
    return (
        "🤖 I can help you with:\n"
        "- Vaccine information\n"
        "- Your child’s vaccination status\n"
        "- Post-vaccination care\n\n"
        "Please ask a vaccination-related question."
    )

# --------------------------------------------------
# UI LAYOUT
# --------------------------------------------------
st.markdown("## 🤖 AI Vaccination Assistant")
st.markdown(
    "Ask any question about **vaccines, your child’s vaccination history, "
    "or post-vaccination care**."
)

st.divider()

question = st.text_input(
    "💬 Ask your question here",
    placeholder="e.g. Has my child completed polio vaccine?"
)

if question:
    answer = generate_response(question)
    st.success(answer)

st.divider()

st.caption(
    "⚕️ This AI assistant provides general guidance only and does not replace a doctor."
)
