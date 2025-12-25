import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Impact Analytics", layout="wide")

st.title("📊 Vaccination Impact Analytics")
st.write(
    """
    This section provides **population-level insights** using the complete
    backend vaccination dataset. These analytics help understand coverage,
    gaps, and public health impact.
    """
)

# --------------------------------------------------
# DATA PATH (FIXED)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "backend_children.csv")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
if not os.path.exists(DATA_PATH):
    st.error(f"CSV NOT FOUND at:\n{DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

if df.empty:
    st.warning("Vaccination dataset is empty.")
    st.stop()

st.subheader("📁 Dataset Overview")
st.write(f"Total Records: **{len(df)}**")
st.dataframe(df.head())

# --------------------------------------------------
# VACCINATION STATUS ANALYSIS
# --------------------------------------------------
st.subheader("💉 Vaccination Coverage")

status_col = None
for col in df.columns:
    if "status" in col.lower():
        status_col = col
        break

if status_col:
    status_counts = df[status_col].value_counts()

    fig, ax = plt.subplots()
    ax.pie(
        status_counts.values,
        labels=status_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

    st.markdown(
        """
        **Observation:**
        - This pie chart represents vaccination completion status.
        - A higher *Completed* percentage indicates strong immunization coverage.
        - *Pending / Missed* vaccinations highlight areas requiring reminders.
        """
    )
else:
    st.info("Vaccination status column not found in dataset.")

# --------------------------------------------------
# AGE DISTRIBUTION
# --------------------------------------------------
st.subheader("👶 Age Distribution")

age_col = next((c for c in df.columns if "age" in c.lower()), None)

if age_col:
    fig, ax = plt.subplots()
    ax.hist(df[age_col].dropna(), bins=10)
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Children")
    st.pyplot(fig)

    st.markdown(
        """
        **Observation:**
        - Most children fall into early age brackets.
        - Helps authorities plan age-specific vaccination drives.
        """
    )
else:
    st.info("Age column not found.")

# --------------------------------------------------
# GENDER DISTRIBUTION
# --------------------------------------------------
st.subheader("🧒 Gender Distribution")

gender_col = next((c for c in df.columns if "gender" in c.lower()), None)

if gender_col:
    gender_counts = df[gender_col].value_counts()

    fig, ax = plt.subplots()
    ax.bar(gender_counts.index, gender_counts.values)
    ax.set_ylabel("Count")
    st.pyplot(fig)

    st.markdown(
        """
        **Observation:**
        - Balanced gender distribution reflects equitable healthcare access.
        - Any skew may indicate reporting or outreach bias.
        """
    )
else:
    st.info("Gender column not found.")

# --------------------------------------------------
# REGION / LOCATION INSIGHTS
# --------------------------------------------------
st.subheader("📍 Regional Distribution")

region_col = next(
    (c for c in df.columns if "state" in c.lower() or "region" in c.lower()),
    None
)

if region_col:
    top_regions = df[region_col].value_counts().head(10)

    fig, ax = plt.subplots()
    ax.barh(top_regions.index, top_regions.values)
    ax.set_xlabel("Number of Children")
    st.pyplot(fig)

    st.markdown(
        """
        **Observation:**
        - Regions with higher counts may have better reporting systems.
        - Low-count regions may need awareness and vaccination drives.
        """
    )
else:
    st.info("Region/State column not found.")

# --------------------------------------------------
# FINAL INSIGHTS
# --------------------------------------------------
st.subheader("📌 Key Insights Summary")

st.markdown(
    """
    - Vaccination coverage data reveals overall program effectiveness.
    - Age and gender insights support inclusive healthcare planning.
    - Regional analytics help target underperforming areas.
    - This module enables **data-driven public health decisions**.
    """
)

st.success("✅ Impact Analytics loaded successfully.")
