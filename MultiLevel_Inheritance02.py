class Animal:
    def Speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def dog(self):
        print("Bhow Bhow")
class BabyDog(Dog):
    def babyDog(self):
        print("Wiping")                
b=BabyDog()        
b.Speak()
b.dog()
b.babyDog()
