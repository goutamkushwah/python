# ===============================
# Dictionary in Python (One File)
# ===============================

# 1. Create Dictionary
student = {
    "name": "Goutam",
    "age": 21,
    "course": "BSc CS"
}
print("Original Dictionary:", student)

# 2. Access Values
print("Name:", student["name"])
print("Age:", student.get("age"))

# 3. Add New Key-Value
student["marks"] = 85
print("After Adding Marks:", student)

# 4. Update Value
student["age"] = 22
print("After Updating Age:", student)

# 5. Delete Key-Value
del student["course"]
print("After Deleting Course:", student)

# 6. Dictionary Methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 7. Loop Through Dictionary
print("\nLooping Dictionary:")
for key, value in student.items():
    print(key, ":", value)

# 8. Check Key Exists
if "name" in student:
    print("\nKey 'name' exists")

# 9. Nested Dictionary
students = {
    1: {"name": "Amit", "age": 20},
    2: {"name": "Ravi", "age": 21}
}
print("\nNested Dictionary:", students)

# 10. Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary Comprehension:", squares)
