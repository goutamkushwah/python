# Date 03-10-2025
# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 
#   set is unmutable and not access by index
s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9

# s = [8, 7, 12, "Harry", [1,2]]   # ✅ Use list
# s[4][0] = 9
# print(s)
