class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age): #constructor method--dundered method
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
print(dog1.name)  
print(dog1.age)   