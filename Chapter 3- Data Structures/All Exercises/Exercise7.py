# Create a list of places to visit (not in alphabetical order)
places_to_visit = ["Tokyo", "Paris", "Saudia Arabia", "Monacco", "Rome"]
#original order
print("Original list:", places_to_visit)
#alphabetical order
print("Sorted list in alphabetical order:", sorted(places_to_visit))
# Check that the original list is still in its original order
print("Original list (still in original order):", places_to_visit)
#reverse alphabetical order
print("Sorted list in reverse alphabetical order:", sorted(places_to_visit, reverse=True))
# Check that the original list is still in its original order
print("Original list (still in original order):", places_to_visit)
# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed list:", places_to_visit)
# Use reverse() again to change the order back to the original
places_to_visit.reverse()
print("Reversed list (back to original order):", places_to_visit)
# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("List in alphabetical order:", places_to_visit)
# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("List in reverse alphabetical order:", places_to_visit)
