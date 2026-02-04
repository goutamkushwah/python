colors = [
     "red",
     "orange",
     "yellow",
     "green",
     "blue",
     "indigo",
     "violet"
]

for color in colors:
     print(color)
# Using enumerate to get index and value
for index, color in enumerate(colors):
     print(index, color)


# for loop with range
print("Numbers from 0 to 4: with for loop and range")
for i in range(5):
     print(i)

# range use 3 parameters: start, stop, step
# range can take one, two, or three parameters
# range(stop)
# range(start, stop)
# range(start, stop, step)

print("Numbers from 0 to 7: with While loop")
a= 0
while a < 8:
        print(a)
        a += 1