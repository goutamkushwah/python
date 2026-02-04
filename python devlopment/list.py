# a= [1,2,3,4,5,6]
# print(a)
# print(type(a))
# print(id(a))
# print(sum(a))  # Output: 21
# squared_a = list(map(lambda x: x**2, a))
# print("Squared a:", squared_a)
# print(a[1])
# print(a[0:4])
# print(a[-1])
# # a.append(7)("After append:", a)
# # a.remove(3)
# print(len(a))
# # a[1]=10
# # print(a)
# # print(a.count(2))
# # print(a[:])

# # fabonacci  series
# def fabonacci(n):
#     fib_series = [0, 1]
#     for i in range(2, n):
#         next_fib = fib_series[i-1] + fib_series[i-2]
#         fib_series.append(next_fib)
#     return fib_series   
# result = fabonacci(10)
# print("Fibonacci series:", result)  

# b=[]
# print("Empty list b:", b)
# print(type(b))
# b=list()
# print("Empty list b using list():", b)
# print(type(b))
# b.append(10)
# b.append(20)
# print("List b after appending 10 and 20:", b)

# d = [1, 2, 3]
# for i in d:
#     print(i)

a=(1,2,3,4,)
(e,b,c,d)=a
print(b)
print(c)
print(d)
print(e)
print(a)