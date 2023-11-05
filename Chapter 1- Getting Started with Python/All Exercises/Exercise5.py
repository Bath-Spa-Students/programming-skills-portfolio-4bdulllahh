# Import the math module to access the value of pi
import math
# Ask the user for the radius of the circle
radius = float(input("Please enter the radius of the circle: "))
# Calculate the area of the circle
area = math.pi * radius**2
# Round the area to 2 decimal places
rounded_area = round(area, 2)
# Print the rounded area
print("The area of the circle with radius", radius, "is:", rounded_area)