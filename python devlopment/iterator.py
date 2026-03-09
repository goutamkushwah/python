my_list = [1,2,3,4]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for loop 
# for i in my_list:
#     print(i)

# infinite ierator
from itertools import count
infinite_iterator = count(1)
for i in range(10):
    print(next(infinite_iterator))