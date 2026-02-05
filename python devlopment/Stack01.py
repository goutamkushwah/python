# using list


# mystack = []
# mystack.append('a')
# mystack.append('b')
# mystack.append('c')
# print(mystack)
# print(mystack.pop())
# print(mystack)
# print(mystack.pop())
# print(mystack)
# print(mystack.pop())
# print(mystack)


# using collections dequqe


# from collections import deque
# mystack = deque()
# mystack.append('a')
# mystack.append('b')
# mystack.append('c')
# print(mystack)
# print(mystack.pop())
# print(mystack)
# print(mystack.pop())
# print(mystack)
# print(mystack.pop())
# print(mystack)

# Stack  and Therading

from queue import LifoQueue
a= LifoQueue(maxsize=3)
print(a.empty())
a.put(1)
a.put(2)
a.put(3)
print(a)
print(a.full())
print(a.get())
print(a.get())
print(a.get())
