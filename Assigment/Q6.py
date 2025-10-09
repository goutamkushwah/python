# WAP to circulate the value of n variable
# 06/08/2025
# Input number of variables
n = int(input("Enter number of variables: "))

# Input the values
values = []
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    values.append(val)

print("\nBefore circulation:")
print(values)

# Circulate: last value moves to front
values = [values[-1]] + values[:-1]

print("\nAfter circulation:")
print(values)
