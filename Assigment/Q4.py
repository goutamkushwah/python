# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponent: a ** b =", a ** b)

print("\nAssignment Operators:")
x = 5
print("Initial value of x:", x)
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 2
print("x *= 2:", x)
x /= 2
print("x /= 2:", x)
x %= 3
print("x %= 3:", x)
x = 5
x **= 2
print("x **= 2:", x)
x //= 2
print("x //= 2:", x)

print("\nComparison Operators:")
a = 10
b = 20
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nBitwise Operators:")
a = 5   # 0101
b = 3   # 0011
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)

print("\nMembership Operators:")
print("1 in x:", 1 in x)
print("4 in x:", 4 in x)
print("2 not in x:", 2 not in x)
a = 2
b = 3
c = 4

print("Without parentheses:")
print("a + b * c =", a + b * c)  # b*c happens first

print("\nWith parentheses:")
print("(a + b) * c =", (a + b) * c)  # a+b happens first

print("\nWith exponentiation:")
print("a + b ** c =", a + b ** c)  # b**c first, then add a

print("\nCombining multiple operators:")
expr = a + b * c / 2 - 1
print("a + b * c / 2 - 1 =", expr)

print("\nWith logical operators:")
print("True or False and False =", True or False and False)  # and > or

print("not True or False =", not True or False)  # not > or
