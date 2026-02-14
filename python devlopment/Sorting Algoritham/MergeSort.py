def MergeSort(lst):
    # Base case: a list of 0 or 1 items is already sorted
    if len(lst) <= 1:
        return lst

    # 1. Split the list in half
    middle = len(lst) // 2
    # 2. Recursively sort both halves (This was missing!)
    left = MergeSort(lst[:middle])
    right = MergeSort(lst[middle:])

    # 3. Merge the sorted halves back together
    return merge(left, right)

def merge(left, right):
    res = []
    # Compare elements from both lists and add the smaller one to res
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0)) # .pop(0) is cleaner than .remove()
        else:
            res.append(right.pop(0))

    # Add any leftover elements (one list will still have items)
    res.extend(left)
    res.extend(right)
    return res

lst = [19, 21, 31, 4, 6, 11, 12, 27]
sorted_lst = MergeSort(lst)
print(sorted_lst)