# Date - 23/11/2025
# Binary search
arr = [10, 20, 30, 40, 50, 60]
x = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Element found at index", mid)
        break
    elif x < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")
