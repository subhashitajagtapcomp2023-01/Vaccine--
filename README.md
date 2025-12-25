Vaccine Sanskar
AI-Powered Child Vaccination Management System

Vaccine Sanskar is an end-to-end smart vaccination tracking system designed to ensure timely, safe, and complete immunization for children.
It combines Python, Machine Learning, Flask, and Streamlit to provide vaccination tracking, reminders, analytics, and risk prediction.

Built as a GDG Hackathon Project by Team TechXplorers

🚀 Problem Statement

Many children miss critical vaccinations due to:

Lack of awareness

No centralized tracking

Missed reminders

Poor follow-up systems

This leads to preventable health risks.

💡 Solution

Vaccine Sanskar provides a digital platform that:

Maintains child vaccination records

Tracks upcoming & completed vaccinations

Sends reminders & notifications

Predicts health risk using ML

Shows analytics & impact dashboards

✨ Key Features

👨‍👩‍👧 Parent & Child Profile Management

💉 Vaccination Schedule & History

⏰ Reminder & Notification System

🤖 AI-based Risk Prediction

📊 Impact Analytics Dashboard

🧾 Digital Vaccination Certificates

🩺 Doctor Notes Module

📚 Vaccine Awareness & Education

🧠 Machine Learning Models

Random Forest – Vaccination risk prediction

Linear Regression – Trend & impact analysis

K-Means Clustering – Risk group classification

Label Encoding & Scaling for preprocessing

Pre-trained models are stored as .pkl files and loaded at runtime.

🛠 Tech Stack

Backend

Python

Flask

Pandas, NumPy

Scikit-learn

Frontend

Streamlit (multi-page application)

Data Storage

CSV files (prototype / hackathon stage)

📁 Project Structure
Vaccine--/
│
├── backend/
│   ├── app.py                     # Flask backend
│   ├── requirements.txt
│   │
│   ├── data/                      # CSV datasets
│   │   ├── 1_users.csv
│   │   ├── 2_children.csv
│   │   ├── 4_vaccination_schedule.csv
│   │   ├── 5_vaccination_history.csv
│   │   ├── 6_doctor_notes.csv
│   │   └── backend_children.csv
│   │
│   ├── models/                    # Trained ML models
│   │   ├── random_forest_vaccination_model.pkl
│   │   ├── linear_regression_model.pkl
│   │   ├── kmeans_risk_model.pkl
│   │   ├── label_encoder.pkl
│   │   └── scaler.pkl
│   │
│   └── Frontend/                  # Streamlit frontend
│       ├── home.py
│       └── pages/
│           ├── 0_Dashboard.py
│           ├── 1_Login.py
│           ├── 2_Add_Baby.py
│           ├── 3_Child_Profile.py
│           ├── 4_Vaccination_Tracker.py
│           ├── 5_Vaccination_Schedule.py
│           ├── 6_Risk_Prediction.py
│           ├── 7_Vaccine_Education.py
│           ├── 8_Doctor_Notes.py
│           ├── 9_Certificate.py
│           ├── 10_Reminders.py
│           ├── 11_Notifications.py
│           ├── 12_Impact_Analytics.py
│           ├── 13_AI_Assistant.py
│           ├── 14_Vaccination_History.py
│           └── 15_Profile_Settings.py
│
├── child_vaccination.ipynb         # ML notebook
├── child_vaccination_raw_dataset.csv
├── README.md
└── .gitignore

⚙️ Setup Instructions (From Scratch)
1️⃣ Clone the Repository
git clone https://github.com/subhashitajagtapcomp2023-01/Vaccine--
cd Vaccine--

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

3️⃣ Install Dependencies
cd backend
pip install -r requirements.txt

▶️ How to Run the Project
🔹 Step 1: Run Backend (Flask)
cd backend
python app.py


Backend will start locally.

🔹 Step 2: Run Streamlit Frontend

Open a new terminal and run:

cd backend/Frontend
streamlit run home.py


The Streamlit app will open automatically in your browser.
