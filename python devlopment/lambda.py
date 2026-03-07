
# lambda
# simple
a=lambda x : x+1
print(a(10))
# add
add_lambda = lambda x,y : x+y
print(add_lambda(5,11))

# (lambda a : a+1)(2)
# ## ans 3

import dis 
add =lambda x,y :x+y
type(add)
dis.dis(add)
print(add)

# map 
num = [1,2,3,4,5]
squares = list(map(lambda x : x**2,num))
print(squares)
print(list(sorted(lambda x : x**2,num)))

