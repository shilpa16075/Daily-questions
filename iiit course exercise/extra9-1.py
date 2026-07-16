order = []
print("Hello Welcome to Shilpa's Cafe 😊")
print("Please make your choices from the menu below:")

end = False
while not end:
    choice_1 = input("Would you like to check the drinks menu or the food menu? \n(Enter 'drinks', 'food', or 'exit'): ").lower()
    
    if choice_1 == 'drinks':
        print("Drinks Menu: \n1. Mocktail \n2. Cold Coffee \n3. Shake \n4. Lemonade")
        choice_1_1 = int(input("Please select a drink by entering the corresponding number (1-4): "))
        if choice_1_1 == 1:
            order.append("Mocktail")
        elif choice_1_1 == 2:
            order.append("Cold Coffee")
        elif choice_1_1 == 3:
            order.append("Shake")
        elif choice_1_1 == 4:
            order.append("Lemonade")
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
        print("Your current order is:", order)
    
    elif choice_1 == 'food':
        print("Food Menu: \n1. Wrap \n2. Garlic Bread \n3. Tacos \n4. Waffles")
        choice_1_2 = int(input("Please select a food item by entering the corresponding number (1-4): "))
        if choice_1_2 == 1:
            order.append("Wrap")
        elif choice_1_2 == 2:
            order.append("Garlic Bread")
        elif choice_1_2 == 3:
            order.append("Tacos")
        elif choice_1_2 == 4:
            order.append("Waffles")
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
        print("Your current order is:", order)

    elif choice_1 == 'exit':
        end = True
    else:
        print("Invalid choice. Please enter 'drinks', 'food', or 'exit'.")

print("\nYour final order is:", order)
print("Thank you for visiting Shilpa's Cafe! Have a great day! 😊")