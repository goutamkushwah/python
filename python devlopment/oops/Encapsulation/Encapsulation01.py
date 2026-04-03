class Person: 
#attributes (public): field and age
    def __init__(self, field, age): 
        self.field = field  
        self.age = age      
  
    # Public method: increase_age
    def increase_age(self, increment): 
        """Increases my age by the given increment."""
        self.age += increment 
        return f"New age: {self.age}" 
# Creating an instance of the class
person1 = Person("Data science", 27) 
# Accessing public attributes directly
print(f"Initial Field: {person1.field}")  # Output: Data Science
print(f"Initial Age: {person1.age}")      # Output: 27
# Calling the public method
result = person1.increase_age(5) 
print(f"Method Result: {result}")  # Output: New age: 32
print(f"Age after method call: {person1.age}") # Output: 32
# Modifying public attributes directly (no restricting access)
person1.field = "Computer Science" 
person1.age = 30
print(f"Field after modification: {person1.field}") # Output: Computer Science
print(f"Age after modification: {person1.age}") # Output: 30
