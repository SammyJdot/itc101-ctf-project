import random
import sys

FLAG = 'itc101{crAck3d_p@s$w0rD_j8DG62Lkc5}'

def caesar_encrypt(text, shift):
    """Encrypts text using a Caesar Cipher with a given shift."""
    encrypted = []
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift_base = 65 if char.isupper() else 97
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted.append(new_char)
        else:
            encrypted.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(encrypted)

def generate_flag():
    """Generates a structured flag for better verification."""
    # prefix = "itc101{"
    # suffix = "}"
    core = "SECURE_" + ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
    # return prefix + core + suffix
    return core

def generate_hint(shift):
    """Provides a hint to the participants."""
    return f"I ate {shift} Caesar salads yesterday!"

def main():
    flag = generate_flag()
    shift = random.randint(1, 25)
    encrypted_flag = caesar_encrypt(flag, shift)
    print("Welcome to the CTF Encryption Challenge!")
    print("Decipher the encrypted string to capture the flag!")
    print("Type 'hint' if you need help or 'quit' to exit.")
    print("Category: Encryption")
    print("Tags: 'encryption', 'crypto', 'cipher', 'decode'")
    print("NOTE: type 'solve' before entering the flag. Flag is randomized each time you run the program")
    print(encrypted_flag)
    hint = 0
    while True:
        user_input = input("\nEnter your command (solve/hint/quit): ").strip().lower()
        
        if user_input == "solve":
            # Ask the user for their decrypted flag
            solution = input("Enter the decrypted flag: ").strip()
            if solution == flag:
                print(f"Correct! The flag is {FLAG}")
                again = input("Do you want to play again? (yes/no)")
                if again == 'yes' or again == 'y':
                    main()
                else:
                    sys.exit()
            else:
                print("Incorrect. Try again.")
        
        elif user_input == "hint":
            if hint == 0:
                print("I love eating Caesar salads!")
                hint += 1
            else:
                print(generate_hint(shift))
        
        elif user_input == "quit":
            print("Thanks for playing! Better luck next time.")
            sys.exit()        
        else:
            print("Invalid command. Please type 'solve', 'hint', or 'quit'.")

if __name__ == "__main__":
    main()
