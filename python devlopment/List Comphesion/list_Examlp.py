nums = [0 for i in range(10)]
print(nums)

# square of number 
squares = [i**2 for i in range(10)]
print(squares)

# Conditional  expression

# if i is even then 0 else 1
a = [0  if i%2 == 0 else 1 for i in range(10)]
print(a)
# if i is divisible by 3 then -1 else i
b= [-1 if i%3 == 0 else i for i in range(10)]
print(b)

#function calls
s= 'Bye'
l = [' '+char.upper() +' 'for char in s]
print(l)

#factoral of number
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *=i
    return num
factorials = [factorial(i) for i in range(1, 10)]
print(factorials)

# more filtering 

evens = [i for i in range(20) if i % 2 == 0]
print(evens)

even_cubes = [i ** 3 for i in range(2, 22) if i % 2 == 0]
print(even_cubes)

# nested loop 
coordinates = [(i, j) for i in range(5) for j in range(4)]
print(coordinates)

coordinates = [(i, j, k) for i in range(3) for j in range(3) for k in range(2)]
print(coordinates)

# 2D list 
g=[[0,0,0]for i in range(3)]
print(g)

h=[[0 for j in range(30)] for i in range(5)]
print(h)