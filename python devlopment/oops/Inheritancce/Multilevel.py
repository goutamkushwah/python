class Animal:
    def speak(self):
        print("Animal is speaking")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")
p=Puppy()
p.speak()
p.bark()
p.weep()                        