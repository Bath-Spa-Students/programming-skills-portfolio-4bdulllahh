def calculate_factorial(number):
    """
    Recursive function to determine the factorial of a given positive integer.

    Parameters:
    - number: Positive integer

    Returns:
    Factorial of the given number
    """
    # Base case: factorial of 0 or 1 is 1
    if number == 0 or number == 1:
        return 1
    else:
        # Recursive case: factorial(n) = n * factorial(n-1)
        return number * calculate_factorial(number - 1)

# Example usage
user_input = int(input("Enter a positive integer: "))

# Verify if the input is a positive integer
if user_input < 0:
    print("Please enter a positive integer.")
else:
    result_factorial = calculate_factorial(user_input)
    print(f"The factorial of {user_input} is: {result_factorial}")

