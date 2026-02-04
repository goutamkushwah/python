import array as arr
# Creating an array of integers
# float_array = arr.array('f', [1.0, 2.0, 3.0, 4.0, 5.0])
# print("Float Array:", float_array)
# char_array = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
# print("Character Array:", char_array)
int_array = arr.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)
# print(type(int_array))

# accesing a element - o(1)

print(int_array[1])

# length of a array

print(len(int_array))

# adding a element - o(n)
 # 1.append
int_array.append(10)
print(int_array) 

# Extend 
int_array.extend([11,12,13])
print(int_array)

# insert
int_array.insert(1,20)
print(int_array)

#removing o(n)
#pop
int_array.pop()
print(int_array)
int_array.pop(1)
print(int_array)

# remove
int_array.remove(11)
print(int_array)


# concating 
a=arr.array('i',[100,200,300])
b=arr.array('i',[400,500,600])
c=a+b
#print(c)

# Slicing 
sliced_array = int_array[1:5]
print("Sliced Array:", sliced_array)
print(int_array[::2])  # Reversed array

# Traversing  --- Lopping through array elements  -- o(n)
for i in int_array:
    print(i)    