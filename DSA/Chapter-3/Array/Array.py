# Yes ✅ Arrays DO exist in Python, but in forms of list tuple.
s = [1, 2, 3, 4, 5]
print(s)
print(type(s))
print(len(s))
print(s[0])
print(s[-1])
for i in s:
    print(i, end=" ")
s[1]= 100
print("\n",s)    
print(s[1:4])
print(s.sort())
