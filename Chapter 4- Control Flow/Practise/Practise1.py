x = float(input("Enter a value for x from 10 to 190: "))
# take input from user

# Initializing y and z with default values
y = 0
z = 0

# Using an if statement to check if x is greater than 100
if x > 100:
    y = 20
    z = 40
    # different messages for different scenarios
    print(f"x is greater than 100. The Value of y is changed into 20, and the value of z is assigned to 40.")
else:
    print(f"x is not greater than 100. The value of y and z does not change.")

# Printing the values of y and z
print("Value of y:", y)
print("Value of z:", z)
