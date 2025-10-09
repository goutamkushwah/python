def sum (a,b):
    print(a+b)

sum(10,20)
sum(30,15)
  
def AddString(s1, s2):
    print(s1+s2)
AddString("Hello","World")

# varable length postiotional args
def fun(*args):
    result = " ".join(args)
    print(result)
fun("Goutam","Kushwah")    
# variable length keyword args
def fun1(s1,s2):
    fun(s1+s2)
fun1(s1="Goutam",s2="Kushwah")
