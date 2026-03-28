#WAP for list, tuple and Dictionary

print("===== LIST OPERATIONS =====")

# Creating a list
nums = [10, 20, 30, 40]
print("Original List:", nums)

# Adding elements
nums.append(50)
print("After append(50):", nums)

nums.insert(1, 15)
print("After insert(1, 15):", nums)

# Extending list
nums.extend([60, 70])
print("After extend([60, 70]):", nums)

# Removing elements
nums.remove(30)
print("After remove(30):", nums)

popped_value = nums.pop()
print("After pop():", nums)
print("Popped value:", popped_value)

# Sorting
nums.sort()
print("After sort():", nums)

nums.reverse()
print("After reverse():", nums)

# Other functions
print("Length of list:", len(nums))
print()

#TUPLE
print("===== TUPLE OPERATIONS =====")

# Creating tuple
fruits = ("apple", "banana", "apple")
print("Original Tuple:", fruits)

# Accessing elements
print("First element:", fruits[0])

# Count & index Length
print("Count of apple:", fruits.count("apple"))
print("Index of banana:", fruits.index("banana")) 
print("Length of tuple:", len(fruits))



print("===== DICTIONARY OPERATIONS =====")

# Creating dictionary
student = {
    "name": "Goutam",
    "age": 21,
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Updating value
student["age"] = 22
print("After updating age:", student)

# Removing element
removed_value = student.pop("grade")
print("After pop('grade'):", student)
print("Removed value:", removed_value)

# Dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length of dictionary:", len(student))

