# List of valid months
valid_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

# Taking user input for the month
month = input("Enter the month (e.g., January, February, etc.): ").lower()  # Convert input to lowercase for case-insensitivity

# Checking if the input month is in the list of valid months
if month in valid_months:
    # Using elif statements to determine the season based on the month
    if month in ["december", "january", "february"]:
        season = "Winter" #sets season variable to winter
    elif month in ["march", "april", "may"]:
        season = "Spring" #sets season variable to spring
    elif month in ["june", "july", "august"]:
        season = "Summer" #sets season variable to summer
    elif month in ["september", "october", "november"]:
        season = "Fall"

    # Displaying the result
    print(f"The season for {month.capitalize()} is {season}.")
    #.capitalize so it writes month name in caps
else:
    print("Please check the spelling :).")
