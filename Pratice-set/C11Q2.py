# Date 07-10-2025
# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
class Animals:
    def Speak(self):
        print("Animal Speaking")
class Dog(Animals):
    def bark(self):
        print("Bhow Bhow")
class Pets(Dog):
    def pet(self):
        print("I am a pet")                
p=Pets()
p.Speak()
p.bark()
p.pet()        