def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Requirement: All vanity plates must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Requirement: Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not 2 <= len(s) <= 6:
        return False

    # Requirement: Numbers cannot be used in the middle of a plate; they must come at the end
    if len(s) > 2 and any(char.isalpha() for char in s[2:-1]) and not s[-1].isalpha():
        return False

    # Requirement: The first number used cannot be '0'
    if s[2:].isdigit() and s[2:].startswith('0') and len(set(s[2:])) > 1:
        return False

    # Requirement: No periods, spaces, or punctuation marks are allowed
    if any(char in '. ,;:!?"\'-_/@#$%^&*()[]{}<>|' for char in s):
        return False

    return True


main()
