# palndroam
s = "madam"
l, r = 0, len(s) - 1

while l < r:
    if s[l] != s[r]:
        print("Not Palindrome")
        break
    l += 1
    r -= 1
else:
    print("Palindrome")
# reverse 
s = list("goutam")
print(s)
l,r=0,len(s)-1
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1    
print("".join(s))