# error 
# logical error
# a = 1 / 0

# syntax error 
# print("Hello World"

# try:
#     a = 1 / 0
#     # a = 10 / 2
#     print("Result is:", a)
# except ZeroDivisionError as e:
#     print("Error occurred:", e)

# else:
#     print("No error occurred, result is:", a)
# finally:
#     print("Execution completed.")    


# raise
# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     else:
#         print("Valid age:", age)

# try:
#     age = int(input("Enter your age: "))
#     check_age(age)
# except ValueError as e:
#     print("Error:", e)


# multiple exceptions

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print("Result is:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")
# except Exception as e:
#     print("An unexpected error occurred:", e)

# else:
#     print("No error occurred, result is:", result)
# finally:
#     print("Execution completed.")    

a= int(input("Enter a number betwwen 5 and 9"))
if a<5 or a>9:
    raise Exception("The value is not between 5 and 9")

print("You have entered:", a)