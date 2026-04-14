# Contain Yield
def squares(length):
    for n in range(length):
        yield n ** 2

squares_gen = squares(10)
print(squares_gen) # <generator object squares at 0x7f8b8c3e5c80>     

for square in squares(5):
    print(square)
    
    
squares=(n**2 for n in range(5))
print(squares) # <generator object <genexpr> at 0x7f8b8c3e5d00>for square in squares:
for square in squares:
    print(square)