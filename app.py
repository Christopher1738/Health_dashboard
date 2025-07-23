from flask import Flask, render_template
import os
from datetime import datetime, timedelta
import random
import json

app = Flask(__name__)

def generate_health_data():
    # Generate 30 days of synthetic data
    data = []
    for i in range(30):
        date = (datetime.now() - timedelta(days=(29-i))).strftime('%Y-%m-%d')
        heart_rate = 72 + random.randint(-5, 15)
        blood_oxygen = 95 + random.randint(-3, 3)
        sleep_hours = round(6.5 + random.uniform(-1, 2), 1)
        steps = 5000 + random.randint(-1000, 2000)
        is_anomaly = 1 if (heart_rate > 100 or blood_oxygen < 90) else 0
        
        data.append({
            "date": date,
            "heart_rate": heart_rate,
            "blood_oxygen": blood_oxygen,
            "sleep_hours": sleep_hours,
            "steps": steps,
            "is_anomaly": is_anomaly
        })
    return data

@app.route('/')
def dashboard():
    try:
        return render_template("dashboard.html", data=generate_health_data())
    except Exception as e:
        return f"<h1>Loading Dashboard</h1><p>Refresh in 30 seconds. Error: {str(e)}</p>", 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
