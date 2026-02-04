# function

# built in
numbers = [1, 2, 3, 4, 5]
print(id(numbers))
print(sum(numbers))  # Output: 15
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

#  user defined
# def add(a, b):
#     return a + b
# result = add(3, 5)
# print("The sum is:", result)


# def greet(name):
#     return "Hello, " + name + "!"
# message = greet("Alice")
# print(message)