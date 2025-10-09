# Date 07-10-2025
# Write a program to filter a list of numbers which are divisible by 5.
def divisible5(num):
    if(num % 5 == 0):
        return True
    else:
        return False

a  = [1,2,34234,53,6234235,64343, 65,754,45,55]

f = list(filter(divisible5, a))
print(f)    