# List of sandwich orders
sandwich_orders = ["Cheese Sandwich", "Falefel Sandwich", "Chicken Sandwich", "Steak Sandwich", "Jam Sandwich", "Pizza Sandwich"]

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
#while loop runs until there are sandwiches in the sandwich_order list 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #pop(0) removes the item from the list and moves or assigns it to 'current_sandwich'
    print(f"I made your {current_sandwich}.") #prints sandwich removed
    finished_sandwiches.append(current_sandwich)

# Displaying the finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich) #prints the sandwiches in the 'finished_sandwich' list

#currently eating a grilled cheese sandwich while writing this code :)
