# Create a list of places to visit (not in alphabetical order)
list = ["Tokyo", "Paris", "Saudia Arabia", "Monacco", "Rome"]

#original order
x = list 
print(x)

#alphabetical order
y = sorted(list)
print(y)

# Check that the original list is still in its original order
print(x)

#reverse alphabetical order
z = sorted(list, reverse=True)
print(z)

# Check original list is still in original order
print("Original list:", list)

# Use reverse() to change the order of list
list.reverse()
print(list)

# Use reverse() again to change the order back to original
list.reverse()
print(list)

# Use sort() to change the list to alphabetical order
list.sort()
print(list)

# Use sort() to change the list to reverse alphabetical order
list.sort(reverse=True)
print(list)
