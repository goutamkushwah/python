#WAP for iterator in python

# -------------------------------------
# WAP TO IMPLEMENT ITERATOR IN PYTHON
# -------------------------------------

class MyNumbers:
    
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration


# Creating object
numbers = MyNumbers(5)

# Using iterator
for value in numbers:
    print(value)
