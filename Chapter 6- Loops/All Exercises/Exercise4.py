# List of sandwich orders
sandwich_orders = ["Cheese Sandwich", "Falefel Sandwich", "Chicken Sandwich", "Steak Sandwich", "Jam Sandwich"]

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #pop(0) removes the item from the list 
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

# Displaying the finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
