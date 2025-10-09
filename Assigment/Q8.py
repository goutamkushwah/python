# Q8 Python program to implement all tuple operations
# 12/09/2025
# 1. Tuple creation
tup1 = (1, 2, 3, 4, 5)
tup2 = ("apple", "banana", "cherry")
print("Tuple 1:", tup1)
print("Tuple 2:", tup2)

# 2. Accessing elements
print("First element of tup1:", tup1[0])
print("Last element of tup2:", tup2[-1])

# 3. Slicing
print("Slice tup1 [1:4]:", tup1[1:4])
print("Slice tup2 [:2]:", tup2[:2])

# 4. Concatenation
tup3 = tup1 + tup2
print("Concatenated Tuple:", tup3)

# 5. Repetition
tup4 = tup2 * 2
print("Repetition:", tup4)

# 6. Membership
print("Is 3 in tup1?", 3 in tup1)
print("Is 'mango' in tup2?", "mango" in tup2)

# 7. Iteration
print("Iterating over tup2:")
for item in tup2:
    print(item, end=" ")
print()

# 8. Length
print("Length of tup1:", len(tup1))

# 9. Count & Index
print("Count of 2 in tup1:", tup1.count(2))
print("Index of 'banana' in tup2:", tup2.index("banana"))

# 10. Nested tuple
nested = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested)
print("Access nested element:", nested[1][1])

# 11. Tuple unpacking
a, b, c = ("red", "green", "blue")
print("Unpacked Values:", a, b, c)

# 12. Converting tuple to list (for modification)
temp_list = list(tup2)
temp_list.append("mango")
tup2_modified = tuple(temp_list)
print("Modified Tuple:", tup2_modified)

# 13. min(), max(), sum() with numbers
print("Min of tup1:", min(tup1))
print("Max of tup1:", max(tup1))
print("Sum of tup1:", sum(tup1))

# 14. Sorted tuple (returns a list)
print("Sorted tup1:", sorted(tup1))
print("Sorted tup2:", sorted(tup2))

# 15. Tuple comprehension (actually list -> tuple)
squares = tuple(x**2 for x in range(1, 6))
print("Squares Tuple:", squares)
