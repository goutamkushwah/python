# Example 1: Using range(stop)
# This will generate numbers from 0 up to stop-1
print("Example 1: range(stop)")
for i in range(5):   # Generates numbers 0,1,2,3,4
    print(i)
print("-" * 30)
# Example 2: Using range(start, stop)
# This will generate numbers from start up to stop-1
print("Example 2: range(start, stop)")
for i in range(2, 7):   # Generates 2,3,4,5,6
    print(i)
print("-" * 30)
# Example 3: Using range(start, stop, step)
# Step defines the difference between numbers
print("Example 3: range(start, stop, step)")
for i in range(2, 10, 2):   # Generates 2,4,6,8
    print(i)
print("-" * 30)
# Example 4: Using negative step (counting backwards)
print("Example 4: range(start, stop, negative step)")
for i in range(10, 0, -2):   # Generates 10,8,6,4,2
    print(i)
print("-" * 30)
# Example 5: Converting range to a list
print("Example 5: Convert range to list")
nums = list(range(5))   # Creates list [0,1,2,3,4]
print(nums)
print("-" * 30)
#  Example 6: Using range with len() in loops
# Useful when iterating indexes of a list
print("Example 6: Iterating list with range and len()")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):  # Generates indices 0,1,2
    print("Index:", i, "Fruit:", fruits[i])
print("-" * 30)
