# for i in range(1,11):
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(21):
#     if i==13:
#         break
#     print(i)


# for i in range(21):
#     if i ==13:
#         continue
#     print(i)

# number = [10, 20, 30]
# it = iter(number)   # create an iterator from the list

# print(next(it))  # 10
# print(next(it))  # 20
# print(next(it))  # 30

# stuent = {
#     "name": "John",
#     "age": 21,
#     "courses": ["Math", "CompSci"]
# }
# for students in stuent.keys():
#     print(students)

num = [1,3,5,7,9]
target = 42
for number in num:
    if number == target:
        print("Found the target:", number)
        break
else:
    print("Target not found in the list")    

