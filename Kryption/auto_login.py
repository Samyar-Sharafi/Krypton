import tkinter as tk
from tkinter import messagebox
import json
import os
import base64
from cryptography.fernet import Fernet
import subprocess

# Secure Credential Storage
CREDENTIALS_FILE = "credentials.json"
ENCRYPTION_KEY_FILE = "key.key"

def generate_key():
    """Generates and stores an encryption key."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    """Loads the stored encryption key."""
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        return key_file.read()

generate_key()  # Ensure key exists
fernet = Fernet(load_key())

def save_credentials(site, username, password):
    """Encrypts and saves credentials."""
    encrypted_password = fernet.encrypt(password.encode()).decode()
    credentials = load_credentials()
    credentials[site] = {"username": username, "password": encrypted_password}

    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file)

def load_credentials():
    """Loads stored credentials."""
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    return {}

def auto_login(site):
    """Performs auto-login using stored credentials."""
    credentials = load_credentials()
    if site in credentials:
        username = credentials[site]["username"]
        encrypted_password = credentials[site]["password"]
        password = fernet.decrypt(encrypted_password.encode()).decode()

        # Simulating login via console command
        messagebox.showinfo("Auto-Login", f"Logging into {site}...\nUsername: {username}\nPassword: {password}")

        # Modify subprocess command for real login execution
        subprocess.run(["echo", f"Logging in {site} with {username}"])
    else:
        messagebox.showerror("Error", "Credentials not found for this site.")

# GUI Setup
root = tk.Tk()
root.title("Auto-Login Manager")

tk.Label(root, text="Site URL:").pack()
site_entry = tk.Entry(root)
site_entry.pack()

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def save_action():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if site and username and password:
        save_credentials(site, username, password)
        messagebox.showinfo("Saved", f"Credentials for {site} stored securely!")

tk.Button(root, text="Save Credentials", command=save_action).pack(pady=5)
tk.Button(root, text="Auto Login", command=lambda: auto_login(site_entry.get())).pack(pady=5)

root.mainloop()
