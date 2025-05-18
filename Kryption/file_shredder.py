import os
import random
from tkinter import filedialog, messagebox

def shred_file():
    file_path = filedialog.askopenfilename(title="Select File to Shred")
    if file_path:
        try:
            with open(file_path, "wb") as f:
                f.write(os.urandom(os.path.getsize(file_path)))
            os.remove(file_path)
            messagebox.showinfo("File Shredder", "File securely deleted!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shred file: {e}")

if __name__ == "__main__":
    shred_file()
