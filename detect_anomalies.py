import pandas as pd
from sklearn.ensemble import IsolationForest

# Load data
df = pd.read_csv("smartwatch_data.csv")

# Train anomaly detection model
model = IsolationForest(contamination=0.05, random_state=42)  # 5% anomalies expected
df["is_anomaly"] = model.fit_predict(df[["heart_rate", "blood_oxygen"]])

# Save results
df.to_csv("anomalies_detected.csv", index=False)
print("✅ Anomalies detected: anomalies_detected.csv")