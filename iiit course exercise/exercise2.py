def check_password_strength(password):
    # Conditions check karne ke liye booleans
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    long_enough = len(password) >= 8

    # Strength evaluate karne ka logic
    if long_enough and has_letter and has_number:
        return "Strong"
    elif long_enough and (has_letter or has_number):
        return "Medium"
    else:
        return "Weak"

# User se input lene aur test karne ke liye code
if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    user_password = input("Enter a password to check: ")
    
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")