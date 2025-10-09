# Date 06-10-2025
# Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_number(n):
    if (n==1):
        return 1
    else:
        return n + sum_of_natural_number(n-1)
    
n=int(input("Enter a number: "))
print("The sum of first",n,"natural number is: ",sum_of_natural_number(n))