class Bank:
    def __init__(self, amount):
        self.__balance = amount  # Private variable (__)

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

acc = Bank(5000)
acc.check_balance()
# print(acc.__balance)  # Yeh error dega kyunki balance private hai