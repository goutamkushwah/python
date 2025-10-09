# Using walrus operator 
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") 
# # Output: List is too long (5 elements, expected <= 3)

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f(10, 20, 30, d=40, e=50, f=60)    