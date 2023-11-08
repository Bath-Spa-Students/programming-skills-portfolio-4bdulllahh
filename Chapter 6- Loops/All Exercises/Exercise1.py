topping = ''  # Initializing the variable to enter the loop

while topping.lower() != 'quit':
    topping = input("Enter a topping to add to your pizza (or 'quit' to finish): ")
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza.")

print("Your pizza is ready!")
