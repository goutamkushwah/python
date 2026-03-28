#WAP to implement classes and objects in python

class Student:
    school_name = "JEC College"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Instance method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("School:", Student.school_name)
        print()

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


# Creating objects
student1 = Student("Goutam", 20, 85)
student2 = Student("Rahul", 17, 55)

# Accessing methods
student1.display_details()
print("Grade of", student1.name, ":", student1.calculate_grade())
print()

student2.display_details()
print("Grade of", student2.name, ":", student2.calculate_grade())
print()