def get_recommendations(user_input, prediction):
    recommendations = []

    if prediction == 1:  # High diabetes risk
        recommendations.append("⚠️ High risk of diabetes detected.")
        recommendations.append("✅ Schedule a consultation with your doctor.")
        recommendations.append("🧪 Consider an HbA1c or fasting blood glucose test.")
    else:
        recommendations.append("🟢 Low risk of diabetes at the moment.")
        recommendations.append("✅ Maintain a healthy lifestyle to reduce future risk.")

    # Lifestyle-based suggestions
    if user_input.get("BMI", 0) > 30:
        recommendations.append("🏃 Consider a weight loss plan. High BMI increases diabetes risk.")
    if user_input.get("Smoking") == 1:
        recommendations.append("🚭 Quitting smoking can reduce your risk significantly.")
    if user_input.get("PhysicalActivity") == 0:
        recommendations.append("🏋️‍♂️ Add at least 30 mins of physical activity 5 days a week.")
    if user_input.get("Fruits") == 0:
        recommendations.append("🍎 Eat more fruits and vegetables daily.")
    if user_input.get("HighBP") == 1:
        recommendations.append("💊 Monitor and manage your blood pressure regularly.")

    return recommendations


from recommendation_engine import get_recommendations

# Simulated user input
user_input = {
    "BMI": 32.5,
    "Smoking": 1,
    "PhysicalActivity": 0,
    "Fruits": 0,
    "HighBP": 1
}

# Simulated prediction
prediction = 1  # Model says "at risk"

# Get recommendations
recs = get_recommendations(user_input, prediction)

# Display
for rec in recs:
    print("-", rec)
