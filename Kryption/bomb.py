import psutil
import subprocess
import time

MEMORY_LIMIT_MB = 2048  # 1GB memory limit

def get_used_memory():
    """ Returns current memory usage in MB """
    return psutil.virtual_memory().used / (1024 * 1024)

def get_available_memory():
    """ Returns available memory in MB """
    return psutil.virtual_memory().available / (1024 * 1024)

def spawn_instance():
    """ Spawns a new Python process running a GUI """
    return subprocess.Popen(["python", "-c", "import tkinter; tkinter.Tk().mainloop()"])

def main():
    processes = []
    
    # Capture initial memory usage at the start of script execution
    initial_memory = get_used_memory()

    try:
        while True:
            current_memory = get_used_memory()
            available_memory = get_available_memory()

            print(f"Initial Used Memory: {initial_memory:.2f} MB")
            print(f"Current Used Memory: {current_memory:.2f} MB")
            print(f"Available Memory: {available_memory:.2f} MB")
            
            # **New Stop Condition:**
            # - Stop spawning if the used memory has increased by 1GB
            # - OR if less than 1GB of free memory remains
            if (current_memory >= initial_memory + MEMORY_LIMIT_MB) or (available_memory <= MEMORY_LIMIT_MB):
                print("Memory limit reached! Stopping instance creation.")
                break  # Stops new instances from being created
            
            # Spawn a process and add it to the list
            proc = spawn_instance()
            processes.append(proc)

            time.sleep(1)  # Pause to avoid excessive rapid launching

    except KeyboardInterrupt:
        print("\nManual stop detected! Cleaning up...")
    
    finally:
        print("Terminating all spawned processes...")
        for proc in processes:
            proc.terminate()  # Gracefully close all instances

if __name__ == "__main__":
    main()
