def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# To print factorials from 1 to 100  
for i in range(1, 101):
       print(f"the factorial of {i} is : {factorial(i)}")