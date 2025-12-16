# Max Min problem
a =[3,5,1,8,2,7,4,6]
max = max(a)
min = min(a)
# print("Max:", max)
# print("Min:", min)
maximum = a[0]
minimum = a[0]
for num in a:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Max:", maximum)
print("Min:", minimum)        