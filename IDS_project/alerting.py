from datetime import datetime
from colorama import Fore, Style

def send_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] [ALERT] {message}"
    print(Fore.RED + alert_message + Style.RESET_ALL)
    with open("logs/intrusion_logs.txt", "a") as log_file:
        log_file.write(alert_message + "\n")
