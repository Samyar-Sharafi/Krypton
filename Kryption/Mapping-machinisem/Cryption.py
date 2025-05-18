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
    reverse_mapping = {}

    if os.path.exists(mapping_file):
        with open(mapping_file, "r") as f:
            for line in f:
                parts = line.strip().split(" -> ")
                if len(parts) == 2:  # Ensures correct formatting
                    original, encrypted = parts
                    fixed_mapping[original] = encrypted
                    reverse_mapping[encrypted] = original
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
            reverse_mapping = {v: k for k, v in fixed_mapping.items()}

            with open(mapping_file, "w") as f:
                for char, mapped_char in fixed_mapping.items():
                    f.write(f"{char} -> {mapped_char}\n")

            print("✅ New mapping file 'mapping.txt' created.")
        else:
            print("❌ No mapping file found! Exiting...")
            exit()  # Stop execution if user declines mapping creation

    return fixed_mapping, reverse_mapping

def encrypt(text, fixed_mapping):
    """Encrypts text using fixed mapping. Leaves spaces and unknown characters unchanged."""
    return ''.join(fixed_mapping.get(char, char) for char in text)

def decrypt(encrypted_text, reverse_mapping):
    """Decrypts text using reverse mapping. Leaves spaces and unknown characters unchanged."""
    return ''.join(reverse_mapping.get(char, char) for char in encrypted_text)

# Load mappings
fixed_mapping, reverse_mapping = load_mappings()

while True:
    action = input("\n🔹 Type E for Encrypt, D for Decrypt, or Q to Quit: ").strip().lower()

    if action == "e":
        text = input("📝 Enter text to encrypt: ")
        print("🔒 Encrypted:", encrypt(text, fixed_mapping))
    elif action == "d":
        encrypted_text = input("📝 Enter text to decrypt: ")
        print("🔑 Decrypted:", decrypt(encrypted_text, reverse_mapping))
    elif action == "q":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid input! Please enter 'E', 'D', or 'Q'.")

    clear_console()  # Clear console after every two inputs
