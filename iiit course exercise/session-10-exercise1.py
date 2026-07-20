print("Welcome to the Canteen!")
print("Select a Restaurant:")
print("1 = Main Dining")
print("2 = Express Bites")
print("3 = Green Leaf Cafe")

restaurant_choice = input("Enter restaurant choice (1, 2, or 3): ")

if restaurant_choice in ["1", "2", "3"]:
    print("\nMenu:")
    print("1 = Rice & curry")
    print("2 = Pasta")
    print("3 = Sandwich")
    
    meal_choice = input("Enter meal choice (1, 2, or 3): ")
    
    if meal_choice == "1":
        print("Your meal: Rice & curry")
    elif meal_choice == "2":
        print("Your meal: Pasta")
    elif meal_choice == "3":
        print("Your meal: Sandwich")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")