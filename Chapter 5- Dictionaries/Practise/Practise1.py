# Creating a dictionary to store information about yourself
myself_info = {
    "name": "Abdullah",
    "age": 18,
    "gender": "Male",
    "occupation": "Student",
    "location": "United Arab Emirates, Umm al Qwain",
    "hobbies": ["Cars", "Gaming", "Sleeping"],
    "favorite_color": "Blue",
}

# Accessing and printing information from the dictionary
print("Name:", myself_info["name"])
print("Age:", myself_info["age"])
print("Gender:", myself_info["gender"])
print("Occupation:", myself_info["occupation"])
print("Location:", myself_info["location"])
print("Hobbies:", ", ".join(myself_info["hobbies"]))
print("Favorite Color:", myself_info["favorite_color"])
