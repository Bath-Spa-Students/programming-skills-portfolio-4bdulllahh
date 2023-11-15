# Take input from the user five times
input = []
for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    input.append(value)

# Typecast to string, int, and float
string_variable = str(input[0])
int_variable = int(input[1])
float_variable = float(input[2])

# Print the variables
print("\nVariables:")
print(f"String Variable: {string_variable}")
print(f"Integer Variable: {int_variable}")
print(f"Float Variable: {float_variable}")
