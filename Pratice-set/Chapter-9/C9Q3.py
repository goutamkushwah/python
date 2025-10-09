# Date 06-10-2025
# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.
def table(n):
    table = ""
    for i in range(1, 11):
       table += f"{n} x {i} = {n*i}\n"
    f= open("Pratice-set/Chapter-9/Table.txt", "a")    
    with open(f"Pratice-set/Chapter-9/Tables/Tables_{n}.txt", "w") as f:
        f.write(table)
for i in range(2, 21):
    table(i)