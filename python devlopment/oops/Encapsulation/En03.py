class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):  # Getter
        return self._age
    @age.setter
    def age(self, value):  # Setter
        if value > 0:
            self._age = value
person = Person(27)
print(person.age)  # Output: 27
person.age = 50
print(person.age)  # Output: 50