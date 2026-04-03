# print(dir(int))

num=10
res = num.__add__(5) 
print(res)

class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'


num=12
val = int.__str__(num)
print(type(val))        