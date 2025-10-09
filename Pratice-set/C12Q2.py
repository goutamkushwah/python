# Date 07-10-2025
# Write a program to print third, fifth and seventh element from a list using enumerate 
# function
l = [1, 2, 3, 4, 5, 6 ,7 , 8]
for i, item in enumerate(l):
    if i in (2, 4, 6):
        print(item)