# Date: 02-10-2025
#WAP for inheritance and all the types of inheritance in python
# 1. Single Inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")  

class Child(Parent):
    def show_child(self):
        print("This is Child class")

print("\n--- Single Inheritance ---")
c = Child()
c.show_parent()
c.show_child()


# 2. Multiple Inheritance
class Father:
    def skills(self):
        print("Father: Knows farming")

class Mother:
    def skills(self):
        print("Mother: Knows cooking")

class Son(Father, Mother):
    def own_skills(self):
        print("Son: Knows programming")

print("\n--- Multiple Inheritance ---")
s = Son()
s.skills()       # method resolution order (Father first)
s.own_skills()


# 3. Multilevel Inheritance
class Grandparent:
    def feature_gp(self):
        print("Grandparent: Honest")

class Parent2(Grandparent):
    def feature_p(self):
        print("Parent: Hardworking")

class Child2(Parent2):
    def feature_c(self):
        print("Child: Smart")

print("\n--- Multilevel Inheritance ---")
c2 = Child2()
c2.feature_gp()
c2.feature_p()
c2.feature_c()


# 4. Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animals can speak in their own way")

class Dog(Animal):
    def bark(self):
        print("Dog: Woof woof!")

class Cat(Animal):
    def meow(self):
        print("Cat: Meow!")

print("\n--- Hierarchical Inheritance ---")
d = Dog()
d.speak()
d.bark()

cat = Cat()
cat.speak()
cat.meow()


# 5. Hybrid Inheritance (Combination)
class A:
    def feature_a(self):
        print("Feature A")

class B(A):
    def feature_b(self):
        print("Feature B")

class C(A):
    def feature_c(self):
        print("Feature C")

class D(B, C):   # Inherits from both B and C (Hybrid: Multilevel + Multiple)
    def feature_d(self):
        print("Feature D")

print("\n--- Hybrid Inheritance ---")
d = D()
d.feature_a()
d.feature_b()
d.feature_c()
d.feature_d()
