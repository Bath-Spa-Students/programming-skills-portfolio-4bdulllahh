# Creating a dictionary
myself_info = {
    "name": "Abdullah",
    "age": 18,
    "gender": "Male",
    "occupation": "Student",
    "location": "United Arab Emirates, Umm al Qwain",
    "hobbies": ["Cars", "Gaming", "Sleeping"],
    "favorite_color": "Red",
}

# Iterating through both keys and values and printing them
print("Keys and values of the dictionary:")
for key, value in myself_info.items():
    print(f"{key}: {value}")
