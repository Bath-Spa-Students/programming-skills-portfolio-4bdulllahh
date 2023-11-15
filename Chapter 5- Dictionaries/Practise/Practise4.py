# Creating a dictionary
myself_info = {
    "name": "Your Name",
    "age": 25,
    "gender": "Female",
    "occupation": "Software Developer",
    "location": "City, Country",
    "hobbies": ["reading", "coding", "traveling"],
    "favorite_color": "Blue",
}

# Iterating through both keys and values and printing them
print("Keys and values of the dictionary:")
for key, value in myself_info.items():
    print(f"{key}: {value}")
