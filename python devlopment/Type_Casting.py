# implicit type casting ( Type promotion )


# a = 5          # integer
# b = 2.5        # float
# c = a + b     # a is promoted to float
# print("The value of c (a + b) is:", c)
# print("The type of c is:", type(c))

# explicit type conversion ( Type casting )

a = 5          # integer
b = '2'
print("The type of b is:", type(b))  
b = int(b)    # converting string to integer
c = a + b
print("The value of c (a + b) is:", c)
print("The type of c is:", type(c))
