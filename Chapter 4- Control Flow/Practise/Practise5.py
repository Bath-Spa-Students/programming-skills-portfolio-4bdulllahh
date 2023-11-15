# Taking user input for the month
month = input("Enter the month (e.g., January, February, etc.): ").lower()  # Convert input to lowercase 


# Using elif statements to determine the season based on the month
if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Invalid month"

# Displaying the result
if season != "Invalid month":
    print(f"The season for {month.capitalize()} is {season}.")
else:
    print("Invalid month entered. Please enter a valid month.")
