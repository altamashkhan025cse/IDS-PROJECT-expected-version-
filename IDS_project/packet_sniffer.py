import scapy.all as scapy
import feature_extraction
import signature_detection
import anomaly_detection

def packet_callback(packet):
    features = feature_extraction.extract_features(packet)
    if features:
        signature_detection.detect_signature(packet)
        anomaly_detection.detect_anomalies(features)

def start_sniffing():
    print("[INFO] Capturing network traffic...")
    scapy.sniff(prn=packet_callback, store=False)
