class Animal:
    def Speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def Bark(self):
        print("Bhow Bhow")        
class Cat(Animal):
    def Meow(self):
        print("Meow Meow")        

c = Cat()     
dog = Dog()   

c.Meow()      
c.Speak()     
dog.Bark()   
dog.Speak()    