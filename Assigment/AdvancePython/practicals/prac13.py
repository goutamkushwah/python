#WAP to implement error and exception handling in python

# -------------------------------------
# PRACTICAL EXAMPLE USING RAISE
# -------------------------------------

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        try:
            # Validation 1: Amount must be positive
            if amount <= 0:
                raise InvalidAmountError("Amount must be positive")

            # Validation 2: Check sufficient balance
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")

            # If validations pass
            self.balance -= amount

        except (InvalidAmountError, InsufficientBalanceError):
            # Re-raise the exception to outer block
            raise

        else:
            print("Withdrawal successful.")
            print("Remaining Balance:", self.balance)

        finally:
            print("Transaction attempted.\n")


# Main Program
try:
    account = BankAccount("Goutam", 5000)

    amt = int(input("Enter amount to withdraw: "))
    account.withdraw(amt)

except InvalidAmountError as e:
    print("Error:", e)

except InsufficientBalanceError as e:
    print("Error:", e)
