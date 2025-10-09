# Python program to implement all dictionary operations
# Date : 12/09/ 2025
# 1. Dictionary creation
student = {"name": "Goutam", "age": 21, "course": "BSc CS"}
print("Original Dictionary:", student)

# 2. Accessing values
print("Name:", student["name"])
print("Age (using get):", student.get("age"))

# 3. Adding new key-value pair
student["roll"] = 101
print("After Adding Roll:", student)

# 4. Modifying values
student["age"] = 22
print("After Updating Age:", student)

# 5. Removing elements
removed = student.pop("course")   # removes by key
print("Removed Value:", removed)
print("After pop:", student)

student.popitem()                 # removes last inserted item
print("After popitem:", student)


# 6. Checking membership
print("Is 'name' a key?", "name" in student)
print("Is 'BSc' a value?", "BSc" in student.values())

# 7. Iterating
print("Iterating keys:")
for key in student:
    print(key, "->", student[key])

print("Iterating items:")
for key, value in student.items():
    print(f"{key}: {value}")

# 8. Length
print("Length of dict:", len(student))

# 9. Copy dictionary
copy_dict = student.copy()
print("Copied Dictionary:", copy_dict)

# 10. Clearing dictionary
copy_dict.clear()
print("After Clear:", copy_dict)

# 11. Nested dictionary
students = {
    1: {"name": "Aman", "age": 20},
    2: {"name": "Riya", "age": 21}
}
print("Nested Dictionary:", students)
print("Access nested value:", students[2]["name"])

# 12. Dictionary methods
marks = {"math": 90, "science": 85}
print("Keys:", marks.keys())
print("Values:", marks.values())
print("Items:", marks.items())

# 13. update() method (merge dictionaries)
extra = {"english": 88}
marks.update(extra)
print("After update:", marks)

# 14. fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("fromkeys dict:", new_dict)

# 15. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Squares Dict:", squares)
