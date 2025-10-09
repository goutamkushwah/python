# Date 06-10-2025
# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

# def pattern(n):
#     for i in range(n, 0, -1):
#         print('*' * i)  

# n = int(input("Enter the number of lines: "))
# pattern(n)

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)


pattern(3)