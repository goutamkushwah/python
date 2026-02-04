# A= {1,2,4,6,8}
# B= {1,2,3,4,5}
# print(A)
# print(type(A))
# print(id(A))

# # union

# # print(A.union(B))
# # print(A|B)

# # intersection

# # print(A.intersection(B))
# # print(A&B)

# # difference

# # print(A.difference(B))
# # print(A-B)


# # print(A.symmetric_difference(B))
# # print(A^B)


# print(A.issubset(B))
# print(A.issuperset(B))
# print(A.isdisjoint(B))
# print(len(A))
# A.add(10)
# print(A)
# A.remove(2)
# print(A)


S1= {'apple', 'banana', 'cherry'}
S2=S1.copy()
S1.clear()
print("Set S1:", S1)
print("Set S2 (copy of S1):", S2)

s = {1, 2, 3}
print(type(s))
for i in s:
    print(i)    

print(2 in s)
print(5 not in s)    