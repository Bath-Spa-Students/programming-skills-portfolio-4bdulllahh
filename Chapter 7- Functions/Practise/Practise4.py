import math #imports the math library for pi 

def compute_circle_area(radius):
    """
    Function to compute the area of a circle.

    Parameters:
    - radius: Radius of the circle

    Returns:
    Calculated area of the circle
    """
    area = math.pi * radius**2 #formula for area of circle
    return area

# Example usage
def main():
    user_radius = float(input("Enter the radius of the circle: "))#ask user for radius

    if user_radius >= 0: #checks if radius is valid
        area_result = compute_circle_area(user_radius)
        print(f"The area of the circle with radius {user_radius} is: {area_result:.2f}")
    else:
        print("Please enter a non-negative radius.")

if __name__ == "__main__":
    main()
