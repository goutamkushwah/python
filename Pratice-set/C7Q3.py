# Date 04-10-2025
# 1. Write a program to print multiplication table of a given number using for loop. 
#  Attempt problem 1 using while loop. 
n = int(input("Enter a number to print its multiplication table: "))
i=1
while(i<=10):
    print(f"{n}*{i}={n*i}")
    i+=1