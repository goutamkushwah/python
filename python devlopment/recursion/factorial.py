# compersion in recursion and loop

# Loop factorial time: 0.003169100033119321
# Recursive factorial time: 0.0033912000944837928

# import timeit

# # Iterative factorial
# def fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# # Recursive factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Measure execution time
# time_loop = timeit.timeit(lambda: fact(5), number=10000)
# time_recursive = timeit.timeit(lambda: factorial(5), number=10000)

# print("Loop factorial time:", time_loop)
# print("Recursive factorial time:", time_recursive)




# By loop

from timeit import timeit 
fact =1
for i in range(1,6):
    fact= fact* i 

print(fact)    
 
# By recursion 

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))    