# Using a for loop with a break statement
for number in range(1, 11):
    print("Current number:", number)
    
    # Check a condition to break the loop
    if number == 5:
        print("Condition met. Exiting the loop.")
        #will break the loop
        break

# This code will continue here after the loop is exited
print("Loop finished.")