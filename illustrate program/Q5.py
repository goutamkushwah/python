# Date 23/11/2025
# GCD
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", math.gcd(a, b))


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
