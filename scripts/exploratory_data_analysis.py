import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/cleaned_data.csv")

# Show class balance
sns.countplot(x="diabetes", data=df)
plt.title("Class Balance")
plt.savefig("eda/class_balance.png")
plt.clf()

# Correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("eda/correlation_heatmap.png")
print("✅ EDA plots saved to eda/")
