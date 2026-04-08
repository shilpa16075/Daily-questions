# Program: Age verification
try:
    age = input("Please enter your age: ")
    age_num = int(age)  # Agar user "abc" likhega toh error aayega
    
    if age_num >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

except ValueError:
    # Ye tab chalega jab string ko number mein convert nahi kiya ja sakega
    print("Error: Invalid input! Please enter numbers only (e.g., 25).")

finally:
    print("Verification attempt finished.")