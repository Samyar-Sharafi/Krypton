import string
import os

characters = string.ascii_lowercase  # Only lowercase letters (no numbers)
message_count = 0  # Track user input count

def clear_console():
    """Clears the console after every two messages, with a notification."""
    global message_count
    message_count += 1
    if message_count % 2 == 0:  # Clear every two messages
        input("\nPress Enter to continue...")  # Pause before clearing
        os.system("cls" if os.name == "nt" else "clear")

def load_mappings():
    """Loads character mappings from the file or gives option to create a new one, skipping invalid lines."""
    mapping_file = "mapping.txt"
    fixed_mapping = {}

    if os.path.exists(mapping_file):
        with open(mapping_file, "r") as f:
            for line in f:
                parts = line.strip().split(" -> ")
                if len(parts) == 2:  # Ensures correct formatting
                    original, encrypted = parts
                    fixed_mapping[original] = encrypted
                else:
                    print(f"⚠ Skipping invalid line in mapping file: {line.strip()}")
        print("✅ Loaded existing mapping.")
    else:
        choice = input("⚠ Mapping file not found! Do you want to create a new mapping? (Y/N): ").strip().lower()
        if choice == "y":
            print("🛠 Creating new default mapping...")

            # Generate default mapping automatically
            letters = string.ascii_lowercase
            fixed_mapping = {char: letters[(i + 3) % len(letters)] for i, char in enumerate(letters)}

            with open(mapping_file, "w") as f:
                for char, mapped_char in fixed_mapping.items():
                    f.write(f"{char} -> {mapped_char}\n")

            print("✅ New mapping file 'mapping.txt' created.")
        else:
            print("❌ No mapping file found! Exiting...")
            exit()  # Stop execution if user declines mapping creation

    return fixed_mapping

def encrypt(text, fixed_mapping):
    """Encrypts text using fixed mapping. Leaves spaces and unknown characters unchanged."""
    return ''.join(fixed_mapping.get(char, char) for char in text)

# Load mappings
fixed_mapping = load_mappings()

while True:
    text = input("\n📝 Enter text to encrypt (or Q to quit): ").strip()
    if text.lower() == "q":
        print("👋 Goodbye!")
        break
    print("🔒 Encrypted:", encrypt(text, fixed_mapping))

    clear_console()  # Clear console after every two inputs
