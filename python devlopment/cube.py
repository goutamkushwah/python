def my_map(my_func, my_iter):
    result = []
    for i in my_iter:
        new_value = my_func(i)
        result.append(new_value)
    return result
nums = [1,2,3,4,5]
cubes = my_map(lambda x : x**3, nums)
print(cubes)