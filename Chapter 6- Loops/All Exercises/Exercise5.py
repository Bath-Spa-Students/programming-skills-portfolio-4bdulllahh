# Initial list of sandwich orders
sandwich_orders = ["Cheese Sandwich", "Falafel Sandwich", "Pastrami Sandwich", "Chicken Sandwich", "Steak Sandwich", "Pastrami Sandwich", "Jam Sandwich", "Pastrami Sandwich"]

# Ensure the 'Pastrami Sandwich' appears at least three times
while sandwich_orders.count('Pastrami Sandwich') >= 3:
    print("Sorry, the deli has run out of Pastrami Sandwich.")
    while 'Pastrami Sandwich' in sandwich_orders:
        sandwich_orders.remove('Pastrami Sandwich')

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    if current_sandwich != 'Pastrami Sandwich':
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)

# Displaying the finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#Still eating that Grilled cheese Sandwich