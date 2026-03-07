def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Have a nice day")
    return mfx
@greet
def hello():
    print("Hello world")
@greet
def add(a,b):
    print(a+b)
hello()
#add(5,6)

