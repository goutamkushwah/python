class Animal:
    def walk(self):
        print("Animal is walking")
class Eating:
    def eat(self):
        print("Animal is eating")        

class Dog(Animal, Eating):
    def bark(self):
        print("Dog is barking")
d =Dog()
d.walk()
d.eat()
d.bark()                