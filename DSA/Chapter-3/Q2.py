# remove duplicate
s = [1,2,2,3,4,4,5,6,7,7,8,9,9,10]
# s = list(set(s))
# print(s)
print("Original List:", s)
res = []
for i in s:
    if i not in res :
        res.append(i)
print("List after removing duplicates:", res)