# Date - 23/11/2025
# Insertion Sort
arr = [5, 3, 8, 4, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

print("Sorted array =", arr)
