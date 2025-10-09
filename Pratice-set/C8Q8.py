# Date 06-10-2025
# Write a python function to print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {n}: {multiplication_table(n)}")        