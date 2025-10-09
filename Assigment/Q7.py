# Q7 Python program to implement all common list operations
# 12/09/2025
# 1. List creation
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# 2. Accessing elements
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

# 3. Modifying elements
fruits[1] = "blueberry"
print("After Modification:", fruits)

# 4. Adding elements
fruits.append("orange")       # add at end
print("After Append:", fruits)

fruits.insert(1, "grape")     # insert at index
print("After Insert:", fruits)

# 5. Extending list
more_fruits = ["mango", "pineapple"]
fruits.extend(more_fruits)
print("After Extend:", fruits)

# 6. Removing elements
fruits.remove("cherry")   # remove by value
print("After Remove:", fruits)

popped = fruits.pop()     # remove last element
print("Popped Element:", popped)
print("After Pop:", fruits)

del fruits[0]             # delete by index
print("After del:", fruits)

# 7. Searching elements
print("Index of mango:", fruits.index("mango"))
print("Is banana in list?", "banana" in fruits)

# 8. Counting
print("Count of mango:", fruits.count("mango"))

# 9. Sorting
nums = [5, 2, 9, 1, 7]
nums.sort()               # ascending
print("Sorted Asc:", nums)

nums.sort(reverse=True)   # descending
print("Sorted Desc:", nums)

# 10. Reversing
nums.reverse()
print("Reversed:", nums)

# 11. Slicing
print("First three:", fruits[:3])
print("From index 2:", fruits[2:])
print("With step 2:", fruits[::2])

# 12. Copying
copy_list = fruits.copy()
print("Copied List:", copy_list)

# 13. Clearing list
copy_list.clear()
print("After Clear:", copy_list)

# 14. Nested lists
nested = [["a", "b"], [1, 2, 3]]
print("Nested List:", nested)
print("Access Nested:", nested[1][2])

# 15. List comprehensions
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
