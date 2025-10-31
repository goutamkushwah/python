# Date 31/10/2025
# WAP for error & exception handling in python.
try:
    # Taking user input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid integers only.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("Division performed successfully!")

finally:
    print("Program execution completed.")
