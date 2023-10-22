guests = ["Robin Williams", "Keanu Reeves", "Rowan Atkinson"]

# Print the guest who can't make it
guest_cant_make_it = "Robin Williams"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Replace the guest who can't make it with a new person
new_guest = "Audrey Hepburn"
guests[guests.index(guest_cant_make_it)] = new_guest

# Generate new invitations
print(f"Dear", new_guest, " I would like to invite you to dinner.")