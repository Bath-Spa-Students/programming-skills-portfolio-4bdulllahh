def check_prime(number):
    """
    Function to determine if a given number is prime.

    Parameters:
    - number: Integer to be evaluated

    Returns:
    True if the number is prime, False otherwise
    """
    if number <= 1: #to check if number less than or equal to 1 
        return False  # Numbers less than or equal to 1 are not considered prime

    for i in range(2, int(number**0.5) + 1): #creates range
        if number % i == 0:
            return False  # If the number is divisible by any number in the given range, it's not prime

    return True  # If no divisors are found, the number is considered prime

# Example usage
user_input = int(input("Enter a number to determine if it's prime: ")) #ask user for input

if check_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
