# Import the math module to access the value of pi
import math

# Ask the user for the radius of the circle
radius = float(input("Please enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Print the calculated area
print("The area of the circle with radius", radius, "is:", area)