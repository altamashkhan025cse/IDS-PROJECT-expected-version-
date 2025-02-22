from flask import Flask, render_template, jsonify, request
import json
import os
import subprocess
from dotenv import load_dotenv  # Import the load_dotenv function

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

LOG_FILE = "logs/anomalies.json"
NETWORK_LOG_FILE = "logs/network_logs.json"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/anomalies')
def anomalies():
    return render_template('anomalies.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/api/anomalies')
def get_anomalies():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            try:
                anomalies = json.load(file)
            except json.JSONDecodeError:
                anomalies = []
    else:
        anomalies = []
    return jsonify(anomalies)

@app.route('/api/logs')
def get_logs():
    if os.path.exists(NETWORK_LOG_FILE):
        with open(NETWORK_LOG_FILE, "r") as file:
            try:
                logs = json.load(file)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []
    return jsonify(logs)

@app.route('/api/turn_off_ids', methods=['POST'])
def turn_off_ids():
    # Get username and password from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Verify admin credentials
    if username == os.getenv('ADMIN_USERNAME') and password == os.getenv('ADMIN_PASSWORD'):
        try:
            # Add logic to stop the IDS program (e.g., kill the process)
            subprocess.run(["pkill", "-f", "anomaly_detector.py"])
            return jsonify({"success": True, "message": "IDS program turned off successfully."})
        except Exception as e:
            return jsonify({"success": False, "message": str(e)})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
