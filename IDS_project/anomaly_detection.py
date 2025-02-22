import joblib
import json
import time
from alerting import send_alert

MODEL_PATH = "models/ids_model.pkl"
ANOMALY_LOG_FILE = "logs/anomalies.json"

try:
    model = joblib.load(MODEL_PATH)
    print("[INFO] Model loaded successfully.")
except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
    model = None

def log_anomaly(details):
    try:
        with open(ANOMALY_LOG_FILE, "r") as file:
            anomalies = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        anomalies = []

    anomalies.append(details)

    with open(ANOMALY_LOG_FILE, "w") as file:
        json.dump(anomalies, file, indent=4)

def detect_anomalies(features):
    if model is None:
        print("[ERROR] Model not loaded.")
        return

    prediction = model.predict([features])
    if prediction[0] == 1:
        anomaly = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": features[4],  # Assuming this is the source IP
            "threat": "Anomalous Activity Detected"
        }
        log_anomaly(anomaly)
        send_alert(f"🚨 Anomalous activity detected from {anomaly['source_ip']}!")
