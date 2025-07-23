from flask import Flask, render_template
import pandas as pd
import os
from datetime import datetime, timedelta

app = Flask(__name__)

def get_health_data():
    # Auto-generate data if file doesn't exist
    if not os.path.exists('health_data.csv'):
        dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)]
        data = {
            'date': dates[::-1],
            'heart_rate': [72 + i%20 + (-1)**i*5 for i in range(30)],
            'blood_oxygen': [96 + i%3 - i//10 for i in range(30)],
            'sleep_hours': [6.5 + i%3 - 0.5*(i%7) for i in range(30)],
            'steps': [5000 + i*300 - (i%4)*500 for i in range(30)],
            'is_anomaly': [0]*25 + [1]*5  # 5 random anomalies
        }
        pd.DataFrame(data).to_csv('health_data.csv', index=False)
    
    return pd.read_csv('health_data.csv').to_dict('records')

@app.route('/')
def dashboard():
    try:
        return render_template("dashboard.html", data=get_health_data())
    except Exception as e:
        return f"<h1>Dashboard Loading</h1><p>Initializing... Refresh in 30 seconds. Error: {str(e)}</p>", 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
