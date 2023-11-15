# Using a for loop with a break statement
for number in range(1, 11):
    #will start printing from first number in range
    print("Current number:", number)
    
    # Check a condition to break the loop
    if number == 5:
        #once number in range reaches 5 the loop will end
        print("Exiting the loop.")
        #will break the loop
        break

#code will continue here after the loop is exited
print("Loop finished.")
