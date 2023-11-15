# Taking user input for the speed variable
speed = float(input("Enter the speed value from 1 to 100: "))

# Checking if speed is within the range of 24 to 56
if 24 <= speed <= 56:
    print("Speed is normal.")
else:
    print("Speed is abnormal.")
#56 isn't abnormal but ok 