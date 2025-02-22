import tkinter as tk
from tkinter import messagebox
import threading
import pandas as pd
import scapy.all as scapy
import os
import time

capturing = False
packets_list = []
log_file = "logs/captured_packets.xlsx"

if not os.path.exists("logs"):
    os.makedirs("logs")

def capture_packets():
    global capturing, packets_list
    packets_list = []
    print("[INFO] Packet sniffing started...")
    while capturing:
        packet = scapy.sniff(count=1)
        packets_list.append(packet[0])
        print(f"[DEBUG] Captured: {packet[0].summary()}")

def start_sniffing():
    global capturing
    if capturing:
        messagebox.showinfo("Info", "Already Capturing!")
        return
    capturing = True
    threading.Thread(target=capture_packets, daemon=True).start()
    messagebox.showinfo("Success", "Packet Sniffing Started!")

def stop_sniffing():
    global capturing, packets_list
    capturing = False
    time.sleep(1)
    print(f"[INFO] Packets Captured: {len(packets_list)}")
    if packets_list:
        df = pd.DataFrame([{
            "Time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Packet Summary": pkt.summary()
        } for pkt in packets_list])
        try:
            df.to_excel(log_file, index=False, engine='openpyxl')
            messagebox.showinfo("Success", f"Logs Saved at {log_file}")
            os.system(f'xdg-open "{log_file}"')
        except Exception as e:
            messagebox.showerror("Error", "Failed to save log file!")
    else:
        messagebox.showwarning("Warning", "No Packets Captured!")

root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("400x300")
root.configure(bg="black")

tk.Label(root, text="Intrusion Detection System", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)
tk.Button(root, text="Start Sniffing", font=("Arial", 12), command=start_sniffing, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Stop Sniffing", font=("Arial", 12), command=stop_sniffing, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="gray", fg="white").pack(pady=10)

root.mainloop()
