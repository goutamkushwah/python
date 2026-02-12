# # non recursive way to traverse nested list
# a= [1,2,[3,4],5,[6,7,8]]
# def traverse(lst):
#     for item in lst:
#         if isinstance(item, list):
#             traverse(item)
#         else:
#             print(item)
# print("Non recursive way to traverse nested list")
# traverse(a)   

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

for i in nested:
    for j in i:
        print(j)