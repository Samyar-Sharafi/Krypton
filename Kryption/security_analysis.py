
import os
from tkinter import messagebox

def security_scan():
    weak_passwords = ["123456", "password", "qwerty", "abc123"]
    test_password = "123456"

    if test_password in weak_passwords:
        messagebox.showwarning("Weak Password", "Your password is weak!")
    else:
        messagebox.showinfo("Security Check", "Password strength good.")

if __name__ == "__main__":
    security_scan()
