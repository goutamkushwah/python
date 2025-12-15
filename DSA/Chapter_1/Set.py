# unchangable unordered collection of unique elements
s={1,2,3,4,5,6,7,8,9,10}
print(s)
print(type(s))
print(len(s))
print(3 in s)
s.add(11)
print(s)
s.update([12,13,14])
print(s)
s.remove(5)
print(s)
s.discard(20)  # does not raise error if element not found
print(s)
s.pop()
print(s)
for i in s:
    print(i)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))