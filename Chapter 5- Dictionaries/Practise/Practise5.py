# Two dictionaries to merge
dict1 = {"name": "Abdullah", "age": 30, "city": "New York"}
dict2 = {"occupation": "Engineer", "hobbies": ["reading", "coding"]}

# Merging dictionaries using update() method
merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying it directly
merged_dict.update(dict2)

# Printing the merged dictionary
print("Merged Dictionary:")
print(merged_dict)
