#WAP to implement encapsulation in python

# -------------------------------------
# IMPLEMENTATION OF ENCAPSULATION
# -------------------------------------

class BankAccount:

    def __init__(self, name, balance):
        self.name = name            # Public variable
        self.__balance = balance    # Private variable (Encapsulated)

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully.")

    # Getter method to access private variable
    def get_balance(self):
        return self.__balance


# Creating object
account = BankAccount("Goutam", 1000)

# Accessing public variable
print("Account Holder:", account.name)

# Trying to access private variable directly (will give error if uncommented)
# print(account.__balance)

# Using public methods to modify private data
account.deposit(500)
account.withdraw(300)

# Accessing private variable using getter method
print("Current Balance:", account.get_balance())