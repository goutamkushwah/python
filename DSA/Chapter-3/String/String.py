s= "my name is goutam kushwah"
print(s)
print(len(s))
print(type(s))
print(s[0])
print(s[5])
print(s[-1])
print(s[0:7])
print(s[11:14])
print(s[::2])
print(s[::-1])
for i in s:
    print(i,end=" ")

txt = "name"
if txt in s:
    print(f"\n{txt} is present in s")

if txt not in s:
    print(f"{txt} is not present in s")
print(s.upper())
print(s.lower())
print(s.replace("goutam","kushwah"))
print(s.split(" "))
print(s.strip())
print(s.startswith("my"))

a= "a,b,c"
b="c,d,e"
print(a+b)

print("hello \n world")
name="goutam"
age=21
print(f"my name is {name} and my age is {age}")