import os
import hashlib
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# List of files to monitor
watched_files = ["gui.py", "passy gen(GUI).py", "auto_login.py", "file_shredder.py"]
file_hashes = {}
LOG_FILE = "integrity_log.txt"

# Global monitoring state
monitoring_active = False  

def compute_hash(file):
    """Computes SHA-256 hash of a file."""
    try:
        with open(file, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        return None

def log_change(file):
    """Logs detected file modifications to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {file} modified!\n")

def initialize_hashes():
    """Stores initial file hashes."""
    global file_hashes
    file_hashes = {file: compute_hash(file) for file in watched_files}

def monitor_files():
    """Continuously monitors files without blocking the GUI."""
    if monitoring_active:
        for file in watched_files:
            new_hash = compute_hash(file)
            if file_hashes.get(file) and new_hash != file_hashes[file]:
                messagebox.showwarning("Integrity Alert", f"{file} has been modified!")
                file_hashes[file] = new_hash  # Update stored hash
                log_change(file)  # Log the modification
            
        root.after(5000, monitor_files)  # Schedule next integrity check every 5 sec

def start_monitoring():
    """Starts monitoring loop."""
    global monitoring_active
    monitoring_active = True
    messagebox.showinfo("Monitoring Started", "System Integrity Monitor is now active.")
    monitor_files()

def stop_monitoring():
    """Stops monitoring."""
    global monitoring_active
    monitoring_active = False
    messagebox.showinfo("Monitoring Stopped", "System Integrity Monitor has been disabled.")

# GUI Setup
root = tk.Tk()
root.title("System Integrity Monitor")

tk.Label(root, text="System Integrity Monitor").pack(pady=10)
tk.Button(root, text="Start Monitoring", command=start_monitoring).pack(pady=5)
tk.Button(root, text="Stop Monitoring", command=stop_monitoring).pack(pady=5)

# Initialize hashes before starting
initialize_hashes()
root.mainloop()
