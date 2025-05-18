
import time
import hashlib
from tkinter import messagebox

def crypto_benchmark():
    start_time = time.time()
    sample_data = "test encryption benchmark" * 10000
    hashed_data = hashlib.sha256(sample_data.encode()).hexdigest()
    elapsed_time = time.time() - start_time
    messagebox.showinfo("Crypto Benchmark", f"SHA-256 Execution Time: {elapsed_time:.3f} sec")

if __name__ == "__main__":
    crypto_benchmark()
