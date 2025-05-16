import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/diabetes_binary_health_indicators_BRFSS2015.csv")

# Rename target column
df.rename(columns={"Diabetes_binary": "diabetes"}, inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)
print("✅ Cleaned data saved to data/cleaned_data.csv")
