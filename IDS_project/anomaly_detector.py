import scapy.all as scapy
import pandas as pd
import numpy as np
import joblib
import time
import json
import os

ANOMALY_LOG_FILE = "logs/anomalies.json"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Load or train an anomaly detection model
def train_model():
    normal_data = pd.DataFrame({
        "packet_size": np.random.normal(500, 100, 1000),
        "time_interval": np.random.exponential(0.1, 1000),
        "protocol": np.random.choice([1, 6, 17], 1000)
    })

    model = IsolationForest(contamination=0.05)
    model.fit(normal_data)

    joblib.dump(model, "models/trained_model.pkl")

def load_model():
    if not os.path.exists("models/trained_model.pkl"):
        train_model()
    return joblib.load("models/trained_model.pkl")

model = load_model()

# Packet sniffing and anomaly detection
def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        packet_size = len(packet)
        time_interval = time.time() - packet.time
        protocol = packet[scapy.IP].proto

        packet_data = pd.DataFrame([[packet_size, time_interval, protocol]],
                                   columns=["packet_size", "time_interval", "protocol"])
        
        prediction = model.predict(packet_data)[0]

        if prediction == -1:
            anomaly = {
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "source_ip": packet[scapy.IP].src,
                "threat": "Anomalous Network Activity"
            }

            if os.path.exists(ANOMALY_LOG_FILE):
                with open(ANOMALY_LOG_FILE, "r") as file:
                    try:
                        anomalies = json.load(file)
                    except json.JSONDecodeError:
                        anomalies = []
            else:
                anomalies = []

            anomalies.append(anomaly)

            with open(ANOMALY_LOG_FILE, "w") as file:
                json.dump(anomalies, file, indent=4)

            print(f"🚨 Anomaly Detected: {anomaly}")

def start_sniffing():
    print("🔍 Sniffing started...")
    scapy.sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
