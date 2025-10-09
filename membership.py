x = [1, 2, 3]
y = x        # y refers to the same object as x
z = [1, 2, 3]

print(x in y)   # True (same memory location)
print(x not in z)   # False (different objects, even if values are same)
