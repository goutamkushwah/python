# Build a class Employee. It should support multiple constructors (different ways to initialize an object).

class Employee:
    def __init__(self, name=None, emp_id=None, salary=None):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


# Different ways to create objects (simulating multiple constructors)
e1 = Employee("Goutam")
e2 = Employee("Shiv", 101)
e3 = Employee("Diksha", 102, 50000)

e1.display()
e2.display()
e3.display()