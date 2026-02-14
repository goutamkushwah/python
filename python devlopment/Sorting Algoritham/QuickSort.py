def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is at right place
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Usage
data = [10, 7, 8, 9, 1, 5]
quick_sort(data, 0, len(data) - 1)
print(f"Sorted array: {data}")