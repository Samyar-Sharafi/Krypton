import tkinter as tk
from tkinter import filedialog, messagebox
import os

characters = "abcdefghijklmnopqrstuvwxyz"

# Global mappings
fixed_mapping = {}
reverse_mapping = {}

def load_mappings():
    """Loads mappings from 'mapping.txt' or prompts for import."""
    global fixed_mapping, reverse_mapping

    if os.path.exists("mapping.txt"):
        with open("mapping.txt", "r") as f:
            for line in f:
                parts = line.strip().split(" -> ")
                if len(parts) == 2:
                    original, encrypted = parts
                    fixed_mapping[original] = encrypted
                    reverse_mapping[encrypted] = original
    else:
        messagebox.showwarning("Warning", "Mapping file not found! Please import one.")
    update_display()

def update_display():
    """Displays mappings in the GUI."""
    mapping_text.delete(1.0, tk.END)
    for original, encrypted in fixed_mapping.items():
        mapping_text.insert(tk.END, f"{original} -> {encrypted}\n")

def import_mapping():
    """Imports mappings from a user-selected file."""
    file_path = filedialog.askopenfilename(title="Select Mapping File", filetypes=[("Text files", "*.txt")])
    if file_path:
        global fixed_mapping, reverse_mapping
        fixed_mapping, reverse_mapping = {}, {}
        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split(" -> ")
                if len(parts) == 2:
                    original, encrypted = parts
                    fixed_mapping[original] = encrypted
                    reverse_mapping[encrypted] = original
        update_display()
        messagebox.showinfo("Success", "Mapping imported successfully!")

def export_mapping():
    """Exports current mappings to a user-specified file."""
    file_path = filedialog.asksaveasfilename(title="Save Mapping File", defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            for original, encrypted in fixed_mapping.items():
                f.write(f"{original} -> {encrypted}\n")
        messagebox.showinfo("Success", "Mapping exported successfully!")

def encrypt_text():
    """Encrypts input text."""
    text = input_text.get()
    encrypted = ''.join(fixed_mapping.get(char, char) for char in text)
    output_label.config(text=f"Encrypted: {encrypted}")

def decrypt_text():
    """Decrypts input text."""
    text = input_text.get()
    decrypted = ''.join(reverse_mapping.get(char, char) for char in text)
    output_label.config(text=f"Decrypted: {decrypted}")

# Initialize GUI
root = tk.Tk()
root.title("Cryption v2.0")

# Input Text Field
tk.Label(root, text="Enter Text:").pack()
input_text = tk.Entry(root, width=50)
input_text.pack()

# Encryption & Decryption Buttons
tk.Button(root, text="Encrypt", command=encrypt_text).pack()
tk.Button(root, text="Decrypt", command=decrypt_text).pack()

# Output Label
output_label = tk.Label(root, text="Output:", font=("Arial", 12))
output_label.pack()

# Mapping Display
tk.Label(root, text="Mappings:").pack()
mapping_text = tk.Text(root, height=10, width=50)
mapping_text.pack()

# Import & Export Buttons
tk.Button(root, text="Import Mapping", command=import_mapping).pack()
tk.Button(root, text="Export Mapping", command=export_mapping).pack()

# Load Existing Mappings
load_mappings()

# Start GUI Loop
root.mainloop()

