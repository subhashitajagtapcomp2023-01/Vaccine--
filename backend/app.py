from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime
import os
import joblib

app = Flask(__name__)
CORS(app)

# =====================================================
# LOAD DATASET (SAFE)
# =====================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "child_vaccination_cleaned_dataset.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("Dataset file not found")

df = pd.read_csv(DATA_PATH)

# =====================================================
# SAFE JSON CONVERTER
# =====================================================
def to_json_safe(value):
    if pd.isna(value):
        return None
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, (pd.Timestamp, datetime)):
        return value.strftime("%Y-%m-%d")
    return value

# =====================================================
# LOAD ML MODEL (OPTIONAL, SAFE)
# =====================================================
RISK_MODEL_PATH = os.path.join(BASE_DIR, "models", "kmeans_risk_model.pkl")
risk_model = None

if os.path.exists(RISK_MODEL_PATH):
    try:
        risk_model = joblib.load(RISK_MODEL_PATH)
        print("✅ Risk model loaded")
    except Exception as e:
        print("⚠️ Risk model failed to load:", e)

# =====================================================
# HEALTH CHECK
# =====================================================
@app.route("/")
def home():
    return jsonify({
        "service": "Child Vaccination Management API",
        "status": "Backend running"
    })

# =====================================================
# CHILD PROFILE
# =====================================================
@app.route("/child/<child_id>")
def get_child(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    row = child.iloc[0]
    return jsonify({
        "child_id": row["child_id"],
        "child_name": row["child_name"],
        "age": to_json_safe(row["child_age_years"]),
        "gender": row["gender"],
        "city": row["city"],
        "family_size": to_json_safe(row["number_of_children_in_family"])
    })

# =====================================================
# VACCINATION STATUS
# =====================================================
@app.route("/vaccination/status/<child_id>")
def vaccination_status(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    row = child.iloc[0]
    return jsonify({
        "completed_vaccine": row["completed_vaccine"],
        "pending_vaccines": row["pending_vaccines"],
        "upcoming_vaccination_name": row["upcoming_vaccination_name"],
        "upcoming_vaccination_date": to_json_safe(row["upcoming_vaccination_date"])
    })

# =====================================================
# VACCINATION SCHEDULE
# =====================================================
@app.route("/vaccination/schedule/<child_id>")
def vaccination_schedule(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    row = child.iloc[0]
    return jsonify({
        "next_vaccine": row["upcoming_vaccination_name"],
        "scheduled_date": to_json_safe(row["upcoming_vaccination_date"])
    })

# =====================================================
# MISSED VACCINATIONS
# =====================================================
@app.route("/vaccination/missed/<child_id>")
def missed_vaccinations(child_id):
    child = df[df["child_id"] == child_id]

    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    row = child.iloc[0]

    if pd.isna(row["upcoming_vaccination_date"]):
        return jsonify({"missed": False})

    # Convert string → datetime
    upcoming_date = pd.to_datetime(row["upcoming_vaccination_date"])
    today = datetime.today()

    if upcoming_date < today:
        return jsonify({
            "missed": True,
            "missed_vaccine": to_json_safe(row["upcoming_vaccination_name"]),
            "missed_date": upcoming_date.strftime("%Y-%m-%d")
        })

    return jsonify({"missed": False})

# =====================================================
# VACCINATION HISTORY
# =====================================================
@app.route("/vaccination/history/<child_id>")
def vaccination_history(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    return jsonify({
        "completed_vaccine": child.iloc[0]["completed_vaccine"]
    })

# =====================================================
# NOTIFICATIONS
# =====================================================
@app.route("/notifications/<child_id>")
def notifications(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    row = child.iloc[0]
    return jsonify({
        "message": f"Upcoming vaccination: {row['upcoming_vaccination_name']} on {to_json_safe(row['upcoming_vaccination_date'])}"
    })

# =====================================================
# ML RISK PREDICTION (CRASH-PROOF)
# =====================================================
@app.route("/predict/risk/<child_id>")
def predict_risk(child_id):
    child = df[df["child_id"] == child_id]
    if child.empty:
        return jsonify({"error": "Child not found"}), 404

    # If model is unavailable, return safe default
    if risk_model is None:
        return jsonify({
            "child_id": child_id,
            "risk_level": "Medium",
            "note": "Model unavailable, fallback used"
        })

    row = child.iloc[0]

    # 7-feature vector (matches trained model shape)
    features = np.array([[
        int(row["child_age_years"]),
        int(row["number_of_children_in_family"]),
        1 if row["gender"].lower() == "male" else 0,
        0, 0, 0, 0
    ]])

    cluster = int(risk_model.predict(features)[0])
    risk_map = {0: "Low", 1: "Medium", 2: "High"}

    return jsonify({
        "child_id": child_id,
        "risk_level": risk_map.get(cluster, "Medium")
    })

# =====================================================
# AI ASSISTANT
# =====================================================
@app.route("/ai/assistant", methods=["POST"])
def ai_assistant():
    data = request.get_json()
    question = data.get("question", "").lower()

    if "next" in question or "due" in question:
        return jsonify({
            "answer": "Please check the vaccination schedule section for upcoming vaccines."
        })

    if "risk" in question:
        return jsonify({
            "answer": "Vaccination risk is calculated based on age and family data."
        })

    if "missed" in question or "pending" in question:
        return jsonify({
            "answer": "Some vaccines may be pending. Please check vaccination status."
        })

    return jsonify({
        "answer": "I can help with vaccination schedules, risks, and reminders."
    })

# =====================================================
# RUN SERVER
# =====================================================
if __name__ == "__main__":
    app.run(port=5001, debug=True)
