from scapy.layers.inet import IP, TCP, UDP

def extract_features(packet):
    if packet.haslayer(IP):
        return [
            len(packet),  # Packet length
            packet[IP].ttl,  # Time to live
            1 if packet.haslayer(TCP) else 0,  # TCP flag
            1 if packet.haslayer(UDP) else 0,  # UDP flag
            packet[IP].src,  # Source IP
            packet[IP].dst,  # Destination IP
        ]
    return None
