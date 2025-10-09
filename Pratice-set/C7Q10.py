# Date 04-10-2025
# Write a program to print multiplication table of n using for loops in reversed 
# order. 
# n= int(input("Enter the num : "))
# for i in range(10,0,-1):
#     print(f"{n} X {i} = {n*i}")
n = int(input("Enter the num : "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")