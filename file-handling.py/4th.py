# Program: Adding two inputs
try:
    a = 10
    b = "20"  # Ye string hai, number nahi
    
    # Python number aur string ko (+) nahi kar sakta
    result = a + b 
    print(result)

except TypeError:
    # Ye tab chalega jab data types mismatch honge
    print("Error: Aap ek number aur text ko jodh (add) nahi sakte!")
    print("Tip: Dono ko same type ka hona chahiye.")

else:
    print("Addition successful!")

finally:
    print("Check complete.")