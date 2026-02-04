a = {1:1,2:2, 3:4.5, 6:7.8 }
print(a)
b = dict({4:5, 5:6})
print(b)
c = dict([(7,8), (9,10)])
print(c)
d = dict.fromkeys(['x', 'y', 'z'], 0)
print(d)
e = dict.fromkeys(range(1,4))
print(e)
f = dict(a=1, b=2, c=3)
print(f)
g = dict(zip(['p', 'q', 'r'], [10, 20, 30]))
print(g)
h = dict(enumerate(['apple', 'banana', 'cherry'], start=1))
print(h)

i = {}
i.update({11:12, 13:14})

print(i)