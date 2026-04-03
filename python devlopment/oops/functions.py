# # functions
# def greetings():
#    "This is docstring of greetings function"
#    print ("Hello World")
#    return
# greetings()

# def testfunction(arg):
#    print ("ID inside the function:", id(arg))

# var = "Hello"
# print ("ID before passing:", id(var))
# testfunction(var)

# def testfunction(arg):
#    print ("ID inside the function:", id(arg))
#    arg = arg + 1
#    print ("new object after increment", arg, id(arg))

# var=10
# print ("ID before passing:", id(var))
# testfunction(var)
# print ("value after function call", var)

# def testfunction(arg):
#    print ("Inside function:",arg)
#    print ("ID inside the function:", id(arg))
#    arg=arg.append(100)
   
# var=[10, 20, 30, 40]
# print ("ID before passing:", id(var))
# testfunction(var)
# print ("list after function call", var)

# def greetings(name):# formal arguments
#    "This is docstring of greetings function"
#    print ("Hello {}".format(name))
#    return
   
# greetings("Samay")
# greetings("Pratima")
# greetings("Steven")  # Arguments are the values passed to the function when it is called. In the above example, "Samay", "Pratima", and "Steven" are arguments passed to the greetings function.

# Positional or Required Arguments

#def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return

# # Now you can call printme function
# printme("Hello, World!")

# Keyword Arguments


# def printme(str):
#     "This prints a passed string into this function"
#     print(str)
#     return

# # Now you can call printme function
# printme( str = "My string")
# Default Arguments

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function

# Positional-only Arguments
# def posFun(x, y, /, z):
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(33, 22, z=11) 
# Keyword-only arguments
# def posFun(*, num1, num2, num3):
#     print(num1 * num2 * num3)

# print("Evaluating keyword-only arguments: ")
# posFun(num1=6, num2=8, num3=5) 
# Arbitrary or Variable-length Arguments
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )