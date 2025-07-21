from flask import Flask, render_template, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Verify template folder path
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = template_dir

@app.route('/')
def dashboard():
    try:
        # Verify CSV exists
        csv_path = os.path.join(os.path.dirname(__file__), 'anomalies_detected.csv')
        if not os.path.exists(csv_path):
            return "Error: Data file not found", 404
            
        df = pd.read_csv(csv_path)
        return render_template("dashboard.html", data=df.to_dict("records"))
        
    except Exception as e:
        return f"Error loading data: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
