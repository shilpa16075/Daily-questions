def check_password_strength(password):
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    long_enough = len(password) >= 8

    if long_enough and has_letter and has_number:
        return "Strong"
    elif long_enough and (has_letter or has_number):
        return "Medium"
    else:
        return "Weak"

# Main execution
user_password = input("Enter your password: ")
strength_result = check_password_strength(user_password)
print(f"Password Strength: {strength_result}")