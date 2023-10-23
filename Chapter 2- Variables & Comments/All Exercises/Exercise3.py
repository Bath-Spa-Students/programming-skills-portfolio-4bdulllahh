#name with whitespace on each end 
name = "\t\n   Abdullah Kamran   \t\n"

# Print the name with the whitespace
print("Name with whitespace:")
print(name)

# Print the name after using each stripping function
print("\nStripped Names:")
print(f"Using lstrip(): {name.lstrip()}")
print(f"Using rstrip(): {name.rstrip()}")
print(f"Using strip(): {name.strip()}")