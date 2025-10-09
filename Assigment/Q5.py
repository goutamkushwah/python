# WAP to implement modules and function
#06/08/2025
# Buillt in function
    # input() - get user input
name = input("Enter your name: ")

    # len() - length of string
print("Length of your name:", len(name))

    # type() - get the type of a variable
age = 25
print("Data type of age:", type(age))

    # max(), min(), sum()
numbers = [5, 10, 3, 8, 2]
print("Numbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

    # sorted() - return a sorted list
print("Sorted List:", sorted(numbers))

    # abs() - absolute value
print("Absolute of -7:", abs(-7))

    # round() - round a float number
print("Rounded value of 3.14159:", round(3.14159, 2))

# User define function
# factorial 
n = int(input("Enter the number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is", fact)

# prime 
n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")