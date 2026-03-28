#WAP for all Boolean operations and functions in python

print("Boolean Data Type")
a = True
print("a =", a)
print("Type of a:", type(a))
print()

print("Logical Operators")

# AND
print("True and True  =", True and True)
print("True and False =", True and False)

# OR
print("True or False  =", True or False)
print("False or False =", False or False)

# NOT
print("not True  =", not True)
print("not False =", not False)
print()


print("bool() Function ")
print("bool(1)      =", bool(1))
print("bool(0)      =", bool(0))
print("bool('Hello')=", bool("Hello"))
print("bool('')     =", bool(""))
print("bool([])     =", bool([]))
print("bool([1,2])  =", bool([1,2]))
print()

print("all() Function ")
print("all([True, True, True])  =", all([True, True, True]))
print("all([True, False, True]) =", all([True, False, True]))
print("all([1, 2, 3])           =", all([1, 2, 3]))
print("all([1, 0, 3])           =", all([1, 0, 3]))
print()

print("any() Function ")
print("any([False, False, True]) =", any([False, False, True]))
print("any([0, '', None])        =", any([0, '', None]))

