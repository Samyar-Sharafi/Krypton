import string

# Define the shift amount
shift = 5
characters = string.ascii_letters + string.digits

def create_mappings(shift, reverse=False):
    """Creates fixed encryption and decryption mappings with optional reverse shift."""
    if reverse:
        fixed_mapping = {char: characters[(i - shift) % len(characters)] for i, char in enumerate(characters)}
    else:
        fixed_mapping = {char: characters[(i + shift) % len(characters)] for i, char in enumerate(characters)}
    reverse_mapping = {v: k for k, v in fixed_mapping.items()}
    return fixed_mapping, reverse_mapping

def encrypt(text, fixed_mapping):
    """Encrypt text using fixed mapping."""
    return ''.join(fixed_mapping.get(char, char) for char in text)

def decrypt(encrypted_text, reverse_mapping):
    """Decrypt text using reverse mapping."""
    return ''.join(reverse_mapping.get(char, char) for char in encrypted_text)

while True:
    # User chooses normal or reverse encryption
    mode = input("\nType N for Normal Shift or R for Reverse Shift (or Q to quit): ").strip().lower()
    if mode == "q":
        print("Goodbye!")
        break  # Exit the loop
    reverse_shift = mode == "r"

    # Generate mappings
    fixed_mapping, reverse_mapping = create_mappings(shift, reverse=reverse_shift)

    # User interaction
    First_input = input("Type E for Encrypt, D for Decrypt, or Q to Quit: ").strip().lower()

    if First_input == "e":
        text = input("Enter text to encrypt: ")
        print("Encrypted:", encrypt(text, fixed_mapping))
    elif First_input == "d":
        encrypted_text = input("Enter text to decrypt: ")
        print("Decrypted:", decrypt(encrypted_text, reverse_mapping))
    elif First_input == "q":
        print("Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid input! Please enter 'E', 'D', or 'Q'.")
