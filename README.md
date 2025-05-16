
# 🩺 Personalized Healthcare Risk Prediction System

This project is a machine learning-powered web application that predicts an individual's risk of **diabetes** based on lifestyle, health history, and demographics. It also provides **personalized health recommendations** to help reduce the risk.

---

## 🚀 Features

- ✅ Predicts diabetes risk using a trained XGBoost model
- ✅ Interactive Streamlit web interface
- ✅ Personalized recommendations based on user inputs
- ✅ Realtime model inference
- ✅ Ready for deployment on Streamlit Cloud

---

## 📁 Project Structure

healthcare-risk-prediction/
├── app/
│ └── main.py # Streamlit frontend app
├── models/
│ └── best_model.joblib # Trained ML model
├── scripts/
│ └── train_model.py # Model training script
├── recommendation_engine.py # Personalized recommendation logic
├── requirements.txt # Project dependencies
└── README.md # You're here!

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/healthcare-risk-prediction.git
cd healthcare-risk-prediction


🔹 2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux

🔹 3. Install Dependencies

pip install -r requirements.txt

🔹 4. Train the Model

python scripts/train_model.py
This will save the trained model to models/best_model.joblib.


▶️ Running the App Locally
bash
Copy
Edit
streamlit run app/main.py

Then open: http://localhost:8501

🌐 Free Deployment (Streamlit Cloud)
Push this project to a public GitHub repository

Go to Streamlit Cloud

Click “New App”, link your repo, and set:

bash
Copy
Edit
app/main.py
Click Deploy

🧠 Model Info
Algorithm: XGBoost Classifier

Accuracy: ~86%

ROC AUC Score: 0.82+

Input Features: 21 health/lifestyle features

Output: Binary prediction (1 = High risk of diabetes)

✍️ Author
Name: Zun ul Noor

Guide: ChatGPT (OpenAI)

Date: May 2025

📜 License
This project is licensed under the MIT License.
