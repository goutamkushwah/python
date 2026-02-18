# keyword args
def sum(a,b):
    return a+b
print(sum(a=10,b=20))
print(sum(b=10,a=20))
 
# postional  only
def my_function(name, /):
  print("Hello", name)

my_function("go")

# key word only
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# Attrbaty keyword argumenat
def student_info(*args, **kwargs):
    print("Student Names:")
    for name in args:
        print("-", name)
    
    print("\nDetails:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
student_info("Goutam", "Ravi", "Anita", course="Python", duration="3 months", level="Beginner")

#genrators
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator
for num in count_up_to(5):
    print(num)

 # A simple decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Goutam!")

say_hello()   

