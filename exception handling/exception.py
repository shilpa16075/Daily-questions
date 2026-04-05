# Program: System-level Safety Check
try:
    # Maan lo hum ek aisi file mein likhne ki koshish kar rahe hain 
    # jo 'Read-Only' hai ya jise system ne block kiya hua hai
    with open("/protected_system_file.txt", "w") as file:
        file.write("Hello World")

except PermissionError:
    # Specific error for restricted access
    print("Error: Aapke paas is file ko edit karne ki permission nahi hai.")

except Exception as e:
    # Generic safety net: Kuch bhi aur galat hua toh ye sambhaal lega
    print(f"Oops! Ek unexpected error aaya: {e}")

finally:
    print("System check finished.")