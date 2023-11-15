# Initialize variables
number_of_courses = int(input("Enter the number of courses: "))  # Number of courses
total_marks = float(input("Enter the total marks: "))  # Total marks for all courses
course_marks = []  # List to store marks for each course

# Input: Marks for each course
for i in range(number_of_courses):
    mark = float(input(f"Enter the marks for course {i + 1}: "))
    course_marks.append(mark)

# Calculate average
total_marks_got = sum(course_marks)
average_marks = total_marks_got / number_of_courses

# Calculate percentage
percentage = (total_marks_got / total_marks) * 100

# Print the results
print("\nResults:")
print(f"Average marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
