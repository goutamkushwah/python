# 1
result = sum(i*i for i in range(10))
print(result)

# 2
xvec = [10, 20, 30]
yvec = [7, 5, 3]
dot_product = sum(x*y for x, y in zip(xvec, yvec))
print(dot_product)

# 3
page = ["this is a test", "this test is simple"]
unique_words = set(word for line in page for word in line.split())
print(unique_words)

# 4
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

graduates = [
    Student("Aman", 8.5),
    Student("Riya", 9.2),
    Student("John", 7.8)
]

valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)

# 5
data = 'golf'
print(data[::-1])