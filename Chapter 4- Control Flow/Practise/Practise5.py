# List of valid months
valid_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
 "october", "november", "december"]

# Taking user input for the month
month = input("Enter the month (e.g., January, February, etc.): ").lower()  # Convert input to lowercase for case-insensitivity

# Checking if the input month is in the list of valid months
if month in valid_months:
    # Using elif statements to determine the season based on the month
    if month in ["december", "january", "february"]: #months that come under winter
        season = "Winter" #sets season variable to winter
    elif month in ["march", "april", "may"]: #months that come under spring
        season = "Spring" #sets season variable to spring
    elif month in ["june", "july", "august"]: #months that come under summer
        season = "Summer" #sets season variable to summer
    elif month in ["september", "october", "november"]: #months that come under fall
        season = "Fall" #sets season variable to fall

    # Displaying the result
    print(f"The season for {month.capitalize()} is {season}.")
    #.capitalize so it writes month name in caps
else:
    print("Please check the spelling :).")
