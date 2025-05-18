import tkinter as tk
import subprocess

# Function to open the encryption tool
def open_encryption_tool():
    subprocess.Popen(["python", "gui.py"])  # Replace with the actual filename

# Function to open the password generator
def open_password_generator():
    subprocess.Popen(["python", "passy gen(GUI).py"])  # Replace with the actual filename
# Function to open the bomb Benchmark
def open_bomb_Benchmark():
    subprocess.Popen(["python", "bomb.py"])
    

# GUI setup
root = tk.Tk()
root.title("Tool Launcher")

tk.Label(root, text="Select a tool to open:").pack(pady=10)

encrypt_button = tk.Button(root, text="Open Encryption Tool", command=open_encryption_tool)
encrypt_button.pack(pady=5)

password_button = tk.Button(root, text="Open Password Generator", command=open_password_generator)
password_button.pack(pady=5)

bomb_button = tk.Button(root, text="Open Bomb Benchmark", command=open_bomb_Benchmark)
bomb_button.pack(pady=5)


root.mainloop()
