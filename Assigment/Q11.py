# Date: 02-10-2025
# WAP for encapsulation in python
class Student:
    def __init__(self, name, age, marks):
        self.name = name          # public attribute
        self._age = age           # protected attribute
        self.__marks = marks      # private attribute

    # getter for private variable
    def get_marks(self):
        return self.__marks

    # setter for private variable
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def show(self):
        print(f"Name: {self.name}, Age: {self._age}, Marks: {self.__marks}")


# creating object
s1 = Student("Goutam", 21, 85)

# accessing public
print(s1.name)

# accessing protected (possible but not recommended)
print(s1._age)

# accessing private directly (will give error)
# print(s1.__marks)  ❌ AttributeError

# accessing private via getter
print("Marks:", s1.get_marks())

# updating private via setter
s1.set_marks(92)
s1.show()

# invalid update
s1.set_marks(150)
