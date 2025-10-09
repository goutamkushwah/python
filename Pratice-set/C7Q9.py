# Date 04-10-2025
# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    if i == 1 or i == n:  # First or last row
        print("* " * n)
    else:  # Middle rows
        print("*", end=" ")
        print("  " * (n - 2), end="")
        print("*")