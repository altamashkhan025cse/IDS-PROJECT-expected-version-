from packet_sniffer import start_sniffing
from gui_main import start_gui

def main():
    print("[INFO] Starting Intrusion Detection System...")
    start_gui()  # Or start_sniffing() for CLI

if __name__ == "__main__":
    main()
