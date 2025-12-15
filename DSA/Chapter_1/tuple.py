# unchanable , ordered collection of items And allows duplicate values
t = (1,2,3,4,5,6,7,8,9,10)
print(t)
print(type(t))  
print(len(t))
print(t[0])
print(t[2])
print(t[-1])
print(t[-3])
print(t[1:5])
print(t[::2])
print(t[1:8:3])
mytuple= tuple(("apple","banana","cherry"))
print(mytuple)

for i in t:
    print(i)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

a=(1,2,3,4,5,6,7,8,9,10,10,10)
print(a.count(10))
print(a.index(5))
