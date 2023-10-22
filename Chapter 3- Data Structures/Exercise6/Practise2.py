lists = ["Robin Williams", "Keanu Reeves", "Rowan Atkinson", "Paul Walker"]

print("I can invite only two people for dinner.")

while len(lists) > 2:
    Removed = lists.pop()
    print(f"Sorry, {Removed}, Unfortunatly I can't invite you to dinner due to some Issues.")

for list in lists:
    print(f"Dear {list}, you're still invited, Please do Join us.")

del lists [:]
print("The guest list is now empty:", lists)