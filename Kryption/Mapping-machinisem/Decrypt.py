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
    """Loads character mappings from the file, skipping invalid lines."""
    mapping_file = "mapping.txt"
    reverse_mapping = {}

    if os.path.exists(mapping_file):
        with open(mapping_file, "r") as f:
            for line in f:
                parts = line.strip().split(" -> ")
                if len(parts) == 2:  # Ensures correct formatting
                    original, encrypted = parts
                    reverse_mapping[encrypted] = original
                else:
                    print(f"⚠ Skipping invalid line in mapping file: {line.strip()}")
        print("✅ Loaded existing mapping.")
    else:
        print("❌ Mapping file not found! Please create 'mapping.txt' manually.")
        exit()  # Stop execution since no mapping exists

    return reverse_mapping

def decrypt(encrypted_text, reverse_mapping):
    """Decrypts text using reverse mapping. Leaves spaces and unknown characters unchanged."""
    return ''.join(reverse_mapping.get(char, char) for char in encrypted_text)

# Load mappings
reverse_mapping = load_mappings()

while True:
    encrypted_text = input("\n📝 Enter text to decrypt (or Q to quit): ").strip()
    if encrypted_text.lower() == "q":
        print("👋 Goodbye!")
        break
    print("🔑 Decrypted:", decrypt(encrypted_text, reverse_mapping))

    clear_console()  # Clear console after every two inputs
