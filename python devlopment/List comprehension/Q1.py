#A list is to be created of the first 15 integers, starting at 0, whose nth element is the square of the integer if it is 
# divisible by 4, or otherwise 0.

a= [i ** 2 if i % 4 == 0 else 0 for i in range(15)]
print(a)

# square = [i**2 if i%4==0 else i for i in range(15)]
# print(square)
