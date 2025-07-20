import pandas as pd

df = pd.read_csv("anomalies_detected.csv")

for index, row in df[df["is_anomaly"] == -1].iterrows():
    if row["heart_rate"] > 100:
        print(f"🚨 ALERT at {row['timestamp']}: High heart rate ({row['heart_rate']} bpm)")
    elif row["blood_oxygen"] < 90:
        print(f"🚨 ALERT at {row['timestamp']}: Low blood oxygen ({row['blood_oxygen']}%)")