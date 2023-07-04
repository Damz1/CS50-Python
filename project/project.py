import random
import string


def main():
    password = prompt_user()
    print_password(password)
    print_strength(password)


def prompt_user():
    length = int(input("Enter the length of the password: "))
    include_lowercase = input(
        "might include lowercase letters? (y/n): ").lower() == "y"
    include_uppercase = input(
        "might include uppercase letters? (y/n): ").lower() == "y"
    include_digits = input("might include digits? (y/n): ").lower() == "y"
    include_symbols = input("might include symbols? (y/n): ").lower() == "y"

    return generate_password(
        length, include_lowercase, include_uppercase, include_digits, include_symbols)


def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def print_password(password):
    if password:
        print("Generated Password:", password)


def print_strength(password):
    strength = assess_strength(password)
    print("Password Strength:", strength)


def assess_strength(password):
    strength = "Weak"
    if len(password) >= 8:
        strength = "Medium"
    if len(password) >= 12:
        strength = "Strong"
    return strength


if __name__ == "__main__":
    main()
