md
# Health Dashboard 🩺📊

An interactive dashboard that visualizes health data, detects anomalies, and provides actionable insights using Python and HTML. This project is designed to work with smartwatch data and offers a live deployment via Vercel.
---

## 📁 Features
- Anomaly detection based on health metrics
- CSV data processing and visualization
- HTML dashboard interface
- Deployment-ready setup with GitHub Pages and Vercel

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git (optional, for cloning)

### Clone the Repository
```bash
git clone https://github.com/Christopher1738/Health_dashboard.git
cd Health_dashboard
Install Dependencies
bash
pip install -r requirements.txt
🧑‍💻 How to Run
Step 1: Start the App
bash
python app.py
This will launch the Flask server. Open your browser and go to http://127.0.0.1:5000/ to view the dashboard.

Step 2: Explore Anomalies
Anomalies are detected from smartwatch_data.csv and exported to anomalies_detected.csv.

You can trigger detection manually via detect_anomalies.py or generate_data.py depending on how data flows are defined.

🛠️ File Structure
File	Description
dashboard.html	Core HTML page rendering health metrics
app.py	Flask web server entry point
detect_anomalies.py	Logic for detecting anomalies from health data
generate_data.py	Simulates/ingests smartwatch data
anomalies_detected.csv	Output data after anomaly detection
requirements.txt	Python package dependencies
Procfile	For deployment configuration
📜 License
This project is licensed under the MIT License

👨‍🔬 Author
Created by Christopher1738
