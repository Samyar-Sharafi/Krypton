import tkinter as tk
import subprocess
import psutil
from tkinter import messagebox

def open_tool(tool):
    subprocess.Popen(["python", tool])  # Launch script

def memory_audit():
    used = psutil.virtual_memory().used / (1024 * 1024)
    available = psutil.virtual_memory().available / (1024 * 1024)
    messagebox.showinfo("Memory Audit", f"Used: {used:.2f} MB\nAvailable: {available:.2f} MB")

root = tk.Tk()
root.title("Security Suite")

tk.Label(root, text="Security Tools").pack(pady=10)

tools = {
    "Encryption Tool": "gui.py",
    "Password Generator": "passy gen(GUI).py",
    "Bomb Benchmark": "bomb.py",
    "Crypto Benchmark": "crypto_benchmark.py",
    "System Integrity Monitor": "system_integrity_monitor.py",
    "Security Analysis": "security_analysis.py",
    "File Shredder": "file_shredder.py",
    "Auto-Login": "auto_login.py",
}

for name, script in tools.items():
    tk.Button(root, text=name, command=lambda s=script: open_tool(s)).pack(pady=5)

tk.Button(root, text="Memory Audit", command=memory_audit).pack(pady=5)

root.mainloop()
