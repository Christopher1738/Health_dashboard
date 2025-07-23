from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime, timedelta
import random

# Get absolute path to templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def generate_health_data():
    """Generate perfect dummy data for your dashboard"""
    data = []
    for i in range(30):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        data.append({
            'date': date,
            'timestamp': f"{date} 12:00:00",
            'heart_rate': random.randint(60, 100),
            'blood_oxygen': random.randint(95, 100),
            'sleep_hours': round(random.uniform(6.0, 8.0), 1),
            'steps': random.randint(4000, 10000),
            'is_anomaly': random.choice([0, 0, 0, 1]),  # 25% chance of anomaly
            'activity_level': random.choice(['low', 'moderate', 'high'])
        })
    return data

@app.route('/')
def dashboard():
    # Triple-check template existence
    template_path = os.path.join(TEMPLATE_DIR, 'dashboard.html')
    if not os.path.exists(template_path):
        return f"Template not found at: {template_path}", 404
        
    try:
        return render_template("dashboard.html", data=generate_health_data())
    except Exception as e:
        return send_from_directory(TEMPLATE_DIR, 'dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
