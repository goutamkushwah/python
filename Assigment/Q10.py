#Date: 02/10/2025
#WAP for polymorphism in python
# def add(x, y):
#     return x + y 

# print(add(2, 3))                
# print(add(2.5, 3.5))            
# print(add("Hello ", "World"))  
# print(add("Good ", "Morning"))
# print(add([1, 2], [3, 4]))     
# print(add((1, 2), (3, 4)))     
  
# Base Class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived Classes
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Cow(Animal):
    def speak(self):
        print("Cow moos")

# Polymorphism in Action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()   # Same method name, different output
