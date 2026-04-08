try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number

except ZeroDivisionError:
    # Runs if the user enters 0
    print("Error: You cannot divide by zero!")

except ValueError:
    # Runs if the user enters text instead of a number
    print("Error: That wasn't a valid number.")

else:
    # Runs ONLY if no errors occurred in the 'try' block
    print(f"Success! The result is {result}")

finally:
    # Runs no matter what (even if the program crashes)
    print("Execution complete. Cleaning up resources...")
    