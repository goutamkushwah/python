# Date 06-10-2025
# Write a program using functions to find greatest of three numbers.
def gratest_betwwen_three(a,b,c):
     if(a>b and a>c):
         return a
     elif(b>a and b>c):
      return b  
     else:
        return c

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print("The gratest number is: ",gratest_betwwen_three(a,b,c))