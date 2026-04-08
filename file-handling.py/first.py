# Program: Reading a file safely
try:
    # Hum ek aisi file open karne ki koshish kar rahe hain jo shayad exist na kare
    file_name = "my_notes.txt"
    file = open(file_name, "r")
    
    content = file.read()
    print(content)

except FileNotFoundError:
    # Ye tab chalega agar file computer mein nahi milti
    print(f"Error: '{file_name}' naam ki koi file nahi mili.")

except Exception as e:
    # Kisi bhi aur technical error ke liye
    print(f"Kuch galat hua: {e}")

finally:
    # Important: Agar file open ho gayi thi, toh usey band karna zaroori hai
    # Chahe error aaye ya na aaye
    print("Cleaning up...")