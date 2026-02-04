
# number = [1, 2, 3]
# latter = ["a", "b", "c"]

# zipped = zip(number, latter)

# print(zipped)
# print(type(zipped))
# print(list(zipped))

# a = range(3)
# b = range(5)
# zipped = zip(a, b)
# print(list(zipped))



# from itertools import zip_longest
# a = range(3)
# b = range(5)
# zipped = zip_longest(a, b)
# print(list(zipped))

from itertools import zip_longest
a = range(3)
b = range(5)
zipped = zip_longest(a, b,fillvalue="?")
print(list(zipped))





