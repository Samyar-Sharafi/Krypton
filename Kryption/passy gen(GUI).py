import tkinter as tk
from tkinter import messagebox
import random

# Character pool for password generation
characters = "123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
special_characters = "!@#$%^&*().~`"

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
