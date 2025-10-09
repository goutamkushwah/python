# Date 07-10-2025
# Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    def __mul__(self, other):
           real_part = self.r * c2.r - self.i * c2.i
           imag_part = self.r * c2.i + self.i * c2.r
           return Complex(real_part, imag_part)    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 + c2)
print(c1 * c2)