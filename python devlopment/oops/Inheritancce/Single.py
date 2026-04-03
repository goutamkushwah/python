class Animal:
    def walk(self):
        print("Animal is walking")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d =Dog()
d.walk()
d.bark()                