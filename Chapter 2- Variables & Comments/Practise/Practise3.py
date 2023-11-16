# Take input from the user five times
user_input = []
for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    user_input.append(value)

# Typecast to string, int, and float
string_variable = str(user_input[0])
int_variable = int(user_input[1])
float_variable = float(user_input[2])

# Print the variables
print("\nVariables:")
print(f"String Variable: {string_variable}")
print(f"Integer Variable: {int_variable}")
print(f"Float Variable: {float_variable}")

