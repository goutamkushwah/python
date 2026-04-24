Define an abstract base class Polygon. It should have an abstract method area(). Create derived classes: 
Rectangle → calculates area as length × breadth. Triangle → calculates area as 0.5 × base × height.
from abc import ABC, abstractmethod

# Abstract Base Class
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass


# Derived Class: Rectangle
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Derived Class: Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
r = Rectangle(10, 5)
t = Triangle(6, 4)

print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())