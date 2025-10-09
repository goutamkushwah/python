# Date 04-10-2025
# Write a program to find whether a given number is prime or not.
n= int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if(n%2==0):
            print(n,"is not a prime number")
        
            break
    else:
            print(n,"is a prime number")
           