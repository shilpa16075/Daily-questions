# --- APPROACH 1: Fails because it compares String to Integer ---
house_no = input("what is your house no?: ")

if house_no == 34:  # Mistake: "34" (string) != 34 (int)
    print("you are infront of correct house")
else:
    print("don't stand in front of wrong house")


# --- APPROACH 2: Works because int() converts input to an Integer ---
house_no = int(input("what is your house no? "))

if house_no == 34:  # Success: 34 (int) == 34 (int)
    print("you are infront of correct house")
else:
    print("don't stand in front of wrong house")