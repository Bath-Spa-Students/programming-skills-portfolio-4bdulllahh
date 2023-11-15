# Initialize a variable to store the largest number
largest_number = float('-inf')  # Start with a very small value
#largest_number variable ensures the first number entered will be considered largest 
while True:#creates infinite loop
    # Take user input
    user_input = input("Enter a number (enter '0' to exit): ") 

    # Check if the user wants to exit
    if user_input == '0':
        break

    # Convert the user input to a float
    number = float(user_input)

    # Update the largest number if the current input is greater
    if number > largest_number:
        largest_number = number

# Print the largest number when the loop exits
print("The largest number entered is:", largest_number)
