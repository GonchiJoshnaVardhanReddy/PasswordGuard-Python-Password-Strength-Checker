def is_strong_password(password):
    """
    Checks if a password is strong based on length, complexity, and common patterns.
    :param password: The input password to be checked.
    :return: True if the password is strong, False otherwise.
    """
    # Check password length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, digits, and special characters
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#$%^&*()_+{}[]|\\:;<>,.?/~" for c in password)

    # Check for common patterns (e.g., "password", "123456", etc.)
    common_patterns = ["password", "123456", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        return False

    # Password complexity criteria
    if has_uppercase and has_lowercase and has_digit and has_special_char:
        return True
    else:
        return False

def main():
    user_password = input("Enter a password: ")
    if is_strong_password(user_password):
        print("Strong password! 🚀")
    else:
        print("Weak password. Please choose a stronger one.")

if __name__ == "__main__":
    main()
