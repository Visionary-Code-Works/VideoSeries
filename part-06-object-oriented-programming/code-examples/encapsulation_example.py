# encapsulation_example.py

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
        self.__show_balance()

    def __show_balance(self):  # Private method
        print(f"Balance: {self.__balance}")

# Creating an Account object
account = Account(1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Output: Insufficient funds

# Direct access to __balance is not possible
# print(account.__balance)  # This will raise an AttributeError
