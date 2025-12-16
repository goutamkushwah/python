a = [1,2,3,6,5,4,8,7,9]
# b = (4,5,6,7,8,9,10)
iteam = 5
for  i in a:
    if i == iteam:
        print("item found at index:",a.index(i))
        break 
else:
    print("item not found")