a = [1,2,3,4,5,6,8,7,9]
# b = (4,5,6,7,8,9,10)
iteam = 5
low = 0
high = len(a) - 1
while low <= high:
    mid = (low +high)//2
    if a[mid] == iteam:
        print("item found at index:",mid)
        break
    elif a[mid] <iteam:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("item not found")
