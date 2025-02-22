# **Python-Based Intrusion Detection System (IDS)**

**A lightweight, real-time intrusion detection system that uses signature-based and anomaly-based techniques to detect malicious network activity.**  



## **📌 Table of Contents**  
- [Introduction](#introduction)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [Future Enhancements](#future-enhancements)  
- [Author](#author)  



## **🔹 Introduction**  
This **Intrusion Detection System (IDS)** monitors network traffic for suspicious activities and alerts administrators about potential security threats. It uses **Python, Scapy, Pandas, and Scikit-learn** for packet analysis and machine learning-based anomaly detection.  



## **🌟 Features**  
✔ **Real-time packet sniffing** using Scapy  
✔ **Signature-based detection** of known malicious IPs  
✔ **Anomaly-based detection** using Machine Learning  
✔ **Logging system** for intrusion records  
✔ **Alert mechanism** for detected threats  
✔ **Modular & scalable** architecture  



## **📂 Project Structure** 


IDS_project/
│── logs/
│   ├── intrusion_logs.txt    # Logs of detected intrusions
│
│── models/
│   ├── ids_model.pkl         # Trained ML model for anomaly detection
│   ├── train_model.py        # Script to train the anomaly detection model
│
│── detect_signature/
│   ├── signature_detection.py  # Signature-based detection module
│
│── main.py                 # Entry point of the IDS
│── packet_sniffer.py        # Packet capturing and feature extraction
│── feature_extraction.py    # Extracts network features for analysis
│── anomaly_detection.py     # Machine Learning-based anomaly detection
│── alerting.py              # Sends alerts for detected threats
│── requirement.txt          # Required dependencies
│── README.md                # Documentation file
```



## **⚙ Installation**  
### **1️⃣ Prerequisites**  
Ensure you have **Python 3.8+** installed.  

### **2️⃣ Install Required Libraries**  
Run the following command:  
```sh
pip install -r requirement.txt
```
---

## **🚀 Usage**  
1️⃣ **Run the IDS**  
```sh
python main.py
```
2️⃣ The system will start monitoring network traffic.  

3️⃣ If an attack is detected, it will generate alerts like:  
```sh
[ALERT] Malicious IP detected: 192.168.1.100
[ALERT] Anomalous activity detected: {'packet_size': 1400, 'protocol': 'TCP'}
```

4️⃣ **To stop the IDS**, press `CTRL + C` or **modify `main.py`** to allow stopping via ENTER key.



## **🔍 How It Works?**  
✔ **Packet Sniffing:** Captures network packets using **Scapy**  
✔ **Feature Extraction:** Extracts packet size, IP addresses, protocols, etc.  
✔ **Signature-Based Detection:** Checks packets against a **list of known malicious IPs**  
✔ **Anomaly-Based Detection:** Uses **Machine Learning (Random Forest/KNN)** to detect **unusual network behavior**  
✔ **Alerting System:** Logs and **alerts the user** when threats are found  

---

## **🔮 Future Enhancements**  
🔹 Integrate **firewall rules** to block attacks automatically  
🔹 Improve **anomaly detection** with deep learning  
🔹 Implement a **web-based dashboard** for real-time monitoring  
🔹 Add **email/SMS notifications** for intrusion alerts  



## 👤 Author 
📝 **Vaishnavi Shinde**  
📧 Email: [vgshinde19.com]  

 

