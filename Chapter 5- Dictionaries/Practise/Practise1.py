# Creating a dictionary to store information about yourself
info = {
    "name": "Abdullah",
    "age": 18,
    "gender": "Male",
    "occupation": "Student",
    "location": "United Arab Emirates, Umm al Qwain",
    "hobbies": ["Cars", "Gaming", "Sleeping"],
    "favorite_color": "Red",
}

# Accessing and printing information from the dictionary
print("Name:", info["name"])
print("Age:", info["age"])
print("Gender:", info["gender"])
print("Occupation:", info["occupation"])
print("Location:", info["location"])
print("Hobbies:", ", ".join(info["hobbies"]))
print("Favorite Color:", info["favorite_color"])
