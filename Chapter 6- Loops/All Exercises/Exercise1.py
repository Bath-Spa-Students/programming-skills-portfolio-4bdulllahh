topping = ''  # Initializing the variable to enter the loop
#The while loop continues as long as the condition topping.lower() != 'quit' is true.
#we add .lower to ensure even if the use write 'quit' in caps the code recognises it 
while topping.lower() != 'quit':
    topping = input("Enter a topping to add to your pizza (or 'quit' to finish): ") #Lets the user to input a topping for the pizza or enter 'quit' to finish
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza.")

print("Your pizza is ready!")
#the loop continues back until the user types in 'quit'
#Enjoy your pizza :))
