# list are orderd, changeable, allow duplicate values
# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 8 9   -- positive indexing
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -- negative indexing
a=["apple","banana","cherry","apple","cherry"]
b=[True,False,True,False]
c=[1.2,3.4,5.6,7.8 ]
print(a)
print(b)
print(c)
l= [1,2,3,4,5,6,7,8,9,10]
print(l)
print(type(l))
print(len(l))
# accessing elements
print(l[0])
print(l[2])
print(l[-1])
print(l[-3])
# slicing
print(l[1:5])
print(l[::2])
print(l[1:8:3])
# constructor

mylist= list(("apple","banana","cherry"))
print(mylist)

if "apple" in a:
    print("yes, 'apple' is in the list a")
else:
    print("no, 'apple' is not in the list a")

# l[1]=100
# print(l)        

#loop
for i in l:
    print(i)

# Add
g = [1,2,3]
print(g)
g.append(4)
print(g)
g.insert(1,1.5)
print(g)
g.extend([5,6,7])
print(g)
