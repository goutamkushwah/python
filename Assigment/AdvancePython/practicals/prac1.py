#WAP for working with numeric data in python including integer, float and complex

# Integer, Float and Complex numbers
a = 15          # integer
b = 4.56789     # float
c = 3 + 2j      # complex

print("Original Values:")
print("a =", a)
print("b =", b)
print("c =", c)

print("\nData Types:")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

print("Addition a+b:", a + b)
print("Addition c+ 4 + 3j :", c + (4 + 3j))

# Type Conversion
a_float = float(a)
b_int = int(b)
a_complex = complex(a)

print("After Type Conversion:")
print("a float:", a_float)
print("b integer:", b_int)
print("a complex:", a_complex)

print("\n---------------------------")

# Rounding
rounded_b = round(b)
rounded_b_2 = round(b, 2)

print("Rounding Operations:")
print("Rounded (no precision):", rounded_b)
print("Rounded to 2 decimal places:", rounded_b_2)

print("\n---------------------------")

# Precision Control using formatting
print("Precision Control:")
print("Formatted to 3 decimal places: {:.3f}".format(b))
print(f"Formatted to 4 decimal places: {b:.4f}")
