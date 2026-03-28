#WAP to impelment abstraction in python

from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Abstract method
    @abstractmethod
    def deposit(self, amount):
        pass

    # Abstract method
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Normal method
    def display_balance(self):
        print("Current Balance:", self.balance)
        print()


# Child Class
class SavingsAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(amount, "withdrawn successfully.")


# Creating object
account1 = SavingsAccount("Goutam", 1000)

account1.display_balance()

account1.deposit(500)
account1.display_balance()

account1.withdraw(300)
account1.display_balance()