# Program: Searching for a price in a dictionary
prices = {"apple": 100, "banana": 50, "orange": 80}

try:
    item = input("Enter fruit name to check price: ").lower()
    
    # Agar item dictionary mein nahi hai, toh KeyError aayega
    print(f"The price of {item} is: {prices[item]}")

except KeyError:
    # Ye block tab chalega jab fruit name galat ho
    print("Error: Sorry, ye fruit hamare paas nahi hai.")

except Exception as e:
    # Ye ek generic safety net hai kisi bhi aur error ke liye
    print(f"An unexpected error occurred: {e}")

finally:
    print("Thank you for using our price checker!")