# Function to calculate average and percentage
def calculate_percentage(marks, total_marks):
    # Calculate average
    average = sum(marks) / len(marks)

    # Calculate percentage
    percentage = (sum(marks) / total_marks) * 100

    return average, percentage

# Input: Number of courses
num_courses = int(input("Enter the number of courses: "))

# Input: Marks for each course
course_marks = []
for i in range(num_courses):
    mark = float(input(f"Enter the marks for course {i + 1}: "))
    course_marks.append(mark)

# Input: Total marks
total_marks = float(input("Enter the total marks: "))

# Calculate average and percentage
average, percentage = calculate_percentage(course_marks, total_marks)

# Print the results
print(f"\nAverage marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
