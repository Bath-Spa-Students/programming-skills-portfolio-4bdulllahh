# Define the cost of one USB stick and the girl's budget
usb_stick_cost = 6
budget = 50

# Calculate how many USB sticks she can buy
#we use the // operator which means floor division
num_usb_sticks = budget // usb_stick_cost

# Calculate how many pounds she will have left
#We use the % operator which means 'modulus'
remaining_pounds = budget % usb_stick_cost

# Print the results
print("The girl can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_pounds, "left.")
