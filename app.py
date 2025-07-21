from flask import Flask, render_template
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

def process_health_data():
    # Generate/simulate data if file missing
    if not os.path.exists('health_data.csv'):
        dates = pd.date_range(end=datetime.today(), periods=30).tolist()
        data = {
            'date': [d.strftime('%Y-%m-%d') for d in dates],
            'heart_rate': [72 + i%20 for i in range(30)],
            'blood_oxygen': [96 + i%3 for i in range(30)],
            'sleep_hours': [6.5 + i%3 for i in range(30)],
            'steps': [5000 + i*300 for i in range(30)],
            'is_anomaly': [0]*25 + [1]*5  # 5 anomalies
        }
        pd.DataFrame(data).to_csv('health_data.csv', index=False)
    
    df = pd.read_csv('health_data.csv')
    return df.to_dict('records')

@app.route('/')
def dashboard():
    health_data = process_health_data()
    return render_template("dashboard.html", data=health_data)

if __name__ == '__main__':
    app.run(debug=True)
