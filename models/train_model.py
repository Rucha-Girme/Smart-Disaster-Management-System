import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Sample Training Data
data = {
    "temperature": [25, 30, 35, 40, 28, 32, 38, 26, 29, 36],
    "humidity": [50, 65, 80, 90, 55, 70, 85, 60, 75, 88],
    "rainfall": [20, 60, 120, 250, 15, 100, 220, 30, 90, 180],
    "wind": [10, 25, 45, 90, 12, 35, 80, 18, 40, 70],
    "result": [
        "SAFE",
        "SAFE",
        "MODERATE",
        "HIGH",
        "SAFE",
        "MODERATE",
        "HIGH",
        "SAFE",
        "MODERATE",
        "HIGH"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features
X = df[["temperature", "humidity", "rainfall", "wind"]]

# Target
y = df["result"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save Model
model_path = os.path.join(os.path.dirname(__file__), "disaster_model.pkl")
joblib.dump(model, model_path)

print("✅ Machine Learning model trained successfully!")
print("📁 Model saved at:", model_path)