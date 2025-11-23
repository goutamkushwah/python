# Date - 23/11/2025
# Linear search
arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == x:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
