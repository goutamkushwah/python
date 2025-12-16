# count vowel and constante
s= "hello my name is goutam kushwah"
vowels= "aeiouAEIOU"
v_count=0
c_count=0
b_count=0
for i in s:
    if i in vowels:
        v_count+=1
    elif i==" ":
        b_count+=1
    else:
        c_count+=1
print(f"vowel count is {v_count}")
print(f"constante count is {c_count}")
print(f"blank space count is {b_count}")        
