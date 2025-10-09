#WAP to find distance between two points in a 2D plane
# 23/07/2025
import math

# Input coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output result
print("Distance between the two points =", distance)
