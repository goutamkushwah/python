#write a program to implement polymorphism in python

# Parent Class
class Car:

    def start(self):   # Polymorphic method
        print("Car starts with a key")

    def fuel_type(self):   # Non-polymorphic method (only in parent)
        print("This car uses petrol or diesel")


# Child Class 1
class ElectricCar(Car):

    def start(self):   # Polymorphic method (overriding)
        print("Electric car starts with a button")

    def battery_capacity(self):   # Non-polymorphic method
        print("Battery capacity is 75 kWh")


# Child Class 2
class SportsCar(Car):

    def start(self):   # Polymorphic method (overriding)
        print("Sports car starts with a remote control")

    def turbo(self):   # Non-polymorphic method
        print("Sports car has turbo engine")


# Creating objects
car = Car()
electric = ElectricCar()
sports = SportsCar()

# Polymorphism (same method name, different behavior)
car.start()
electric.start()
sports.start()

print()

# Non-polymorphic methods
car.fuel_type()
electric.battery_capacity()
sports.turbo()