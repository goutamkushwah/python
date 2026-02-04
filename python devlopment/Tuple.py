# a=(1,2,3,4,5,6)
# print(a)
# print(type(a))
# print(id(a))
# print(sum(a))  # Output: 21
# squared_a = list(map(lambda x: x**2, a))
# print("Squared a:", squared_a)
# print(a[1])
# print(a[0:4])
# print(a[-1])

# print(len(a))
# # a[1]=10  # Tuples are immutable, this will raise an error
# # print(a)
# # print(a.count(2))
# # print(a[:])


# empty_tuple = ()
# print("Empty tuple:", empty_tuple)
# print(type(empty_tuple))
# empty_tuple = tuple()
# print("Empty tuple using tuple():", empty_tuple)
# print(type(empty_tuple))
# single_element_tuple = (10,)
# print("Single element tuple:", single_element_tuple)
# print(type(single_element_tuple))

# copy 
# students = ('Alice', 'Bob', 'Charlie')
# students_copy = students[:]
# print("Original tuple:", students)
# print("Copied tuple:", students_copy)
# print(id(students)==id(students_copy))

# from copy import deepcopy
# original_tuple = (1, 2, [3, 4], (5, 6))
# shallow_copied_tuple = original_tuple[:]
# deep_copied_tuple = deepcopy(original_tuple)
# print("Original tuple:", original_tuple)
# print("Shallow copied tuple:", shallow_copied_tuple)
# print("Deep copied tuple:", deep_copied_tuple)

# d = (1, 2, 3)
# for i in d:
#     print(i)

# print(d.count(2))
# print(d.index(3))
# e = (4, 5, 6)
# print(sorted(e))
# print(min(e))
# print(max(e))

# Tuple unpacking
a=(1,2,3,4,)
(e,b,c,d)=a
print(b)
print(c)
print(d)
print(e)
print(a)

# tupl1 =  1,
# print(type(tupl1))
# print(tupl1)