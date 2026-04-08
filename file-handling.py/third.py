# Program: Withdraw money from ATM
balance = 1000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        # Hum khud error generate kar rahe hain kyunki balance kam hai
        raise ValueError("Insufficient balance!")
    
    if amount <= 0:
        raise ValueError("Amount must be positive!")

    balance -= amount
    print(f"Withdrawal successful! Remaining balance: {balance}")

except ValueError as e:
    # Jo message 'raise' ke saath likha tha, wo 'e' mein aa jayega
    print(f"Transaction Failed: {e}")

finally:
    print("Thank you for using our ATM.")