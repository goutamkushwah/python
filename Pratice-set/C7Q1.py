# Date 04-10-2025
# Write a program to print multiplication table of a given number using for loop. 

num=int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")