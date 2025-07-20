from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Your routes (keep your existing routes here)
@app.route('/')
def dashboard():
    try:
        df = pd.read_csv("anomalies_detected.csv")
        return render_template("dashboard.html", data=df.to_dict("records"))
    except Exception as e:
        return f"Error loading data: {str(e)}", 500

# Add this at the bottom
if __name__ == '__main__':
    # Development server (runs only when executing app.py directly)
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    # Production mode (for Gunicorn)
    pass