def factorial(n):
    """
    Recursive function to calculate the factorial of a given positive integer.

    Parameters:
    - n: Positive integer

    Returns:
    Factorial of n
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Example usage
user_input = int(input("Enter a positive integer: "))

# Check if the input is a positive integer
if user_input < 0:
    print("Please enter a positive integer.")
else:
    result_factorial = factorial(user_input)
    print(f"The factorial of {user_input} is: {result_factorial}")
