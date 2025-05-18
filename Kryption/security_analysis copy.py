import re
import tkinter as tk
from tkinter import messagebox
import os
import platform
import subprocess

def security_scan(password):
    """Checks password security based on length, symbols, uppercase, and numbers."""
    if len(password) < 7:
        messagebox.showwarning("Weak Password", "Password is too short! Use at least 7 characters.")
    elif not re.search(r'[!@#$%^&*()_+~`]', password):
        messagebox.showwarning("Weak Password", "Password lacks symbols! Include special characters.")
    elif not re.search(r'[A-Z]', password):
        messagebox.showwarning("Weak Password", "Password lacks uppercase letters! Include at least one.")
    elif not re.search(r'\d', password):
        messagebox.showwarning("Weak Password", "Password lacks numbers! Include at least one.")
    else:
        messagebox.showinfo("Security Check", "Password strength good.")

def check_system_password():
    """Scans OS-stored passwords depending on platform."""
    system = platform.system()
    stored_passwords = []

    if system == "Windows":
        try:
            result = subprocess.run(["cmdkey", "/list"], capture_output=True, text=True)
            stored_passwords = [line for line in result.stdout.split("\n") if "Target" in line]
        except Exception:
            messagebox.showerror("Error", "Failed to retrieve Windows credentials.")

    elif system == "Linux":
        if os.path.exists("/var/lib/misc/shadow.passwd"):
            with open("/var/lib/misc/shadow.passwd") as f:
                stored_passwords = f.readlines()
        else:
            messagebox.showinfo("Linux Security", "No system passwords found.")

    elif system == "Darwin":  # macOS
        try:
            result = subprocess.run(["security", "find-generic-password", "-ga", "system"], capture_output=True, text=True)
            stored_passwords = result.stdout.split("\n")
        except Exception:
            messagebox.showerror("Error", "Failed to retrieve macOS keychain credentials.")

    if stored_passwords:
        messagebox.showinfo("System Passwords", f"Found system passwords:\n{stored_passwords[:5]}")
    else:
        messagebox.showinfo("Security Check", "No system-stored passwords detected.")

def user_choice():
    """Prompts user to enter a password manually or scan system credentials."""
    choice = messagebox.askyesno("Security Analysis", "Enter password manually?")
    if choice:
        prompt_manual_entry()
    else:
        check_system_password()

def prompt_manual_entry():
    """GUI for entering a password manually."""
    input_window = tk.Toplevel()
    input_window.title("Enter Password")

    tk.Label(input_window, text="Enter Password:").pack()
    password_entry = tk.Entry(input_window, show="*", width=30)
    password_entry.pack()

    def analyze_password():
        security_scan(password_entry.get())

    tk.Button(input_window, text="Check Password", command=analyze_password).pack()
    input_window.wait_window()  # Ensures the window pauses execution until closed

# Launch GUI
root = tk.Tk()
root.withdraw()  # Hide root window for a clean UI experience
user_choice()