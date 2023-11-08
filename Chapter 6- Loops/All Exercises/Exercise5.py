# Initial list of sandwich orders plus the pastrami Sandwich
sandwich_orders = ["Cheese Sandwich", "Falafel Sandwich", "Pastrami Sandwich", "Chicken Sandwich", "Steak Sandwich", "Pastrami Sandwich", "Jam Sandwich", "Pastrami Sandwich"]

# This section checks if 'Pastrami' appears in the sandwich_orders list at least three 
while sandwich_orders.count('Pastrami Sandwich') >= 3:
    print("Sorry, the deli has run out of Pastrami Sandwich.")
    #enters a loop to remove all partrami sandwiches from the list 
    while 'Pastrami Sandwich' in sandwich_orders:
        sandwich_orders.remove('Pastrami Sandwich')

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)#pop(0) removes sandwich from list 
    #if sandwich is not pastrami it prints that sandwich has been made and adds it to finished_sandwich list 
    if current_sandwich != 'Pastrami Sandwich':
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)

# Displaying the finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#Still eating that Grilled cheese Sandwich :) 