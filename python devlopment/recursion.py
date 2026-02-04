#  recursion

# factorial function using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print("Factorial of 5 is:", fact(5))  # Output: 120