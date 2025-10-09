# Date - 02-10-2025
#WAP for data abstraction in python.
from abc import ABC, abstractmethod

# Define an abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_info(self):
        print("This is a shape.")

# Implement concrete subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage of the abstract and concrete classes
if __name__ == "__main__":
    # Cannot instantiate an abstract class directly
    # shape = Shape() # This would raise a TypeError

    circle = Circle(5)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")
    circle.display_info()

    rectangle = Rectangle(4, 6)
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
    rectangle.display_info()