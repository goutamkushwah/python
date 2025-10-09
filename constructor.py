class Employee: 
    language = "Python"  # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):  # Constructor
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Goutam = Employee("Goutam", 1300000, "JavaScript")
Goutam.name = "Goutam"
print(Goutam.name, Goutam.salary, Goutam.language)

rohan = Employee("Rohan", 1000000, "Python")
rohan.getInfo()
rohan.greet()
