import scapy.all as scapy
import pandas as pd
import os
from alerting import send_alert

attack_signatures = {
    "DDoS": ["SYN Flood", "UDP Flood"],
    "Malware": ["Trojan", "Worm", "Keylogger"],
    "Port Scan": ["Nmap", "Xmas Scan"]
}

log_file = "logs/signature_logs.xlsx"

if not os.path.exists("logs"):
    os.makedirs("logs")

def detect_signature(packet):
    packet_summary = packet.summary()
    for attack_type, signatures in attack_signatures.items():
        for signature in signatures:
            if signature.lower() in packet_summary.lower():
                alert_message = f"{attack_type} detected: {signature}"
                send_alert(alert_message)

def start_signature_detection():
    print("[INFO] Starting signature-based detection...")
    scapy.sniff(prn=detect_signature, store=False)
