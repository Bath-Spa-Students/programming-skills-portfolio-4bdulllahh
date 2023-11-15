def calculate_sum(x, y):
    """
    Function to compute the sum of two numbers.

    Parameters:
    - x: First number
    - y: Second number

    Returns:
    The sum of x and y
    """
    return x + y

# Example usage
input_num1 = float(input("Enter the first number: "))
input_num2 = float(input("Enter the second number: "))

result_sum = calculate_sum(input_num1, input_num2)
print(f"The sum of {input_num1} and {input_num2} is: {result_sum}")
