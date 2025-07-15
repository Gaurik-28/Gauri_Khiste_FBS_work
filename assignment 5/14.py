# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
# Input number of students
num_students = int(input("Enter number of students: "))
percentages = []


for student in range(1, num_students + 1):
    print(f"\nEnter marks for Student {student}:")
    total = 0

    
    for subject in range(1, 6):
        marks = float(input(f"  Subject {subject} marks: "))
        total += marks

    
    percentage = total / 5
    percentages.append(percentage)
    print(f" Percentage of Student {student}: {percentage:.2f}%")


average_percentage = sum(percentages) / num_students
print(f"Average Percentage of all students: {average_percentage:.2f}%")

