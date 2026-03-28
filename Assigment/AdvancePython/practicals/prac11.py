#WAP for generator in python

# -------------------------------------
# WAP TO IMPLEMENT GENERATOR IN PYTHON
# -------------------------------------

def my_generator(n):
    num = 1
    while num <= n:
        yield num
        num += 1


# Creating generator object
gen = my_generator(5)

# Using generator
for value in gen:
    print(value)