import pandas as pd
import numpy as np

# Generate 24 hours of data (1-minute intervals)
timestamps = pd.date_range(start="2024-01-01", periods=1440, freq="min")  # Fixed: 'min' instead of 'T'

# Simulate normal data
heart_rate = np.random.normal(loc=75, scale=10, size=1440).astype(int)
blood_oxygen = np.random.normal(loc=98, scale=1, size=1440).astype(int)

# Add anomalies (e.g., high heart rate)
heart_rate[500:510] = np.random.randint(120, 140, size=10)  # Danger zone!

# Save to CSV
df = pd.DataFrame({"timestamp": timestamps, "heart_rate": heart_rate, "blood_oxygen": blood_oxygen})
df.to_csv("smartwatch_data.csv", index=False)
print("✅ Data generated: smartwatch_data.csv")