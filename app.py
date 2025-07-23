from flask import Flask, render_template
import os
from datetime import datetime, timedelta
import random
import json

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

def generate_health_data():
    """Generate synthetic health data matching your dashboard's expected format"""
    data = []
    today = datetime.now()
    
    for i in range(30):  # 30 days of data
        date = (today - timedelta(days=(29-i))).strftime('%Y-%m-%d')
        
        # Generate realistic metrics with some anomalies
        base_hr = 72 + random.randint(-3, 3)
        hr_variation = random.randint(-5, 15)
        heart_rate = base_hr + hr_variation
        
        blood_oxygen = 96 + random.randint(-3, 3)
        sleep_hours = round(6.5 + random.uniform(-1.5, 1.5), 1)
        steps = 5000 + random.randint(-1500, 2500)
        
        # Mark as anomaly if outside normal ranges
        is_anomaly = 1 if (heart_rate > 100 or heart_rate < 60 or blood_oxygen < 90) else 0
        
        data.append({
            "date": date,
            "timestamp": date + " 12:00:00",  # Needed for your dashboard
            "heart_rate": heart_rate,
            "blood_oxygen": blood_oxygen,
            "sleep_hours": sleep_hours,
            "steps": steps,
            "is_anomaly": is_anomaly,
            "activity_level": random.choice(["low", "moderate", "high"])
        })
    
    return data

@app.route('/')
def dashboard():
    try:
        health_data = generate_health_data()
        
        # Debug: Verify data matches template expectations
        print("Sample data point:", health_data[0])
        print("Templates path:", app.template_folder)
        print("Template exists:", os.path.exists(os.path.join(app.template_folder, 'dashboard.html')))
        
        return render_template("dashboard.html", data=health_data)
        
    except Exception as e:
        return f"""
        <h2>Loading Health Dashboard</h2>
        <div class='alert alert-warning'>
            <p>Refresh in 30 seconds while we initialize your data.</p>
            <p><strong>Technical Details:</strong> {str(e)}</p>
        </div>
        """, 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
