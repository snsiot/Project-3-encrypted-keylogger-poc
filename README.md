# 🔐 Encrypted Keylogger PoC (Educational Use Only)

## 📌 Objective
This is a **proof-of-concept (PoC)** Python keylogger intended for **ethical hacking education and cybersecurity research**. It captures keyboard input, encrypts the data using AES (Fernet), stores it locally, and simulates exfiltration.

---

## ⚙️ Features
- ✅ Keystroke capture via `pynput`
- 🔒 AES encryption via `cryptography.fernet`
- 🕒 Timestamped local logging
- 🛰️ Simulated exfiltration to `localhost`
- 🛑 Kill switch using `ESC` key

---

## 🚀 Usage

### 1. Install Requirements
```bash
pip install -r requirements.txt
