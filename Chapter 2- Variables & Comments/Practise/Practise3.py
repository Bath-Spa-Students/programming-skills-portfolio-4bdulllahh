# Take input from the user five times
input_values = []
for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    input_values.append(value)

# Typecast to string, int, and float
string_variable = str(input_values[0])
int_variable = int(input_values[1])
float_variable = float(input_values[2])

# Print the variables
print("\nVariables:")
print(f"String Variable: {string_variable}")
print(f"Integer Variable: {int_variable}")
print(f"Float Variable: {float_variable}")
