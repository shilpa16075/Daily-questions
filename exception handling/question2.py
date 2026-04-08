# Program: Accessing an item from a list
fruits = ["apple", "banana", "cherry"]

try:
    # Hum 5th item mang rahe hain, par list mein sirf 3 items hain (index 0, 1, 2)
    index = int(input("Enter index number (0-2): "))
    print(f"You picked: {fruits[index]}")

except IndexError:
    # Ye tab chalega jab index list ki range se bahar ho
    print("Error: Wo index list mein hai hi nahi!")

except ValueError:
    # Ye tab chalega jab user number ki jagah text daal de
    print("Error: Please sirf number enter karein.")

finally:
    print("Task completed.")