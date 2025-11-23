# Date - 23/11/2025
# Bubble Sort
arr = [5, 3, 8, 4, 2]

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array =", arr)
