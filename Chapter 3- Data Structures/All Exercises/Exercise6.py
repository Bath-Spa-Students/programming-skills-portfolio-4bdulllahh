# Initial list of guests
guests = ["Robin Williams", "Keanu Reeves", "Rowan Atkinson", "Paul Walker"]

# Print a message about the limited space
print("I can invite only two people for dinner.")

# Use pop() to remove guests one at a time
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print messages to the two remaining guests
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner.")

# Use del to remove the last two names
del guests[:]
print("My guest list is now empty:", guests)
