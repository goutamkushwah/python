# Date 23/11/2025
# circulates the value of n among its digits.
n = int(input("Enter number of variables: "))
vals = []

# taking input
for i in range(n):
    vals.append(input(f"Enter value {i+1}: "))

# rotation
last = vals[-1]
vals = [last] + vals[:-1]

print("After circulation:", vals)
