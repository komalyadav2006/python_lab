
def calculate_statistics(*grades, **student_info):
    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for grade in grades:
        if grade >= 90:
            grade_distribution["A"] += 1
        elif grade >= 80:
            grade_distribution["B"] += 1
        elif grade >= 70:
            grade_distribution["C"] += 1
        elif grade >= 60:
            grade_distribution["D"] += 1
        else:
            grade_distribution["F"] += 1

    return minimum, maximum, average, grade_distribution, student_info


# Taking input from user
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

grades = []

for i in range(n):
    grade = float(input(f"Enter marks for subject {i + 1}: "))
    grades.append(grade)

# Calling function using *args and **kwargs
result = calculate_statistics(
    *grades,
    name=name,
    subjects=n
)

# Tuple unpacking
minimum, maximum, average, distribution, info = result

# Displaying results
print("\n----- Student Statistics -----")
print("Student Name:", info["name"])
print("Number of Subjects:", info["subjects"])
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))

print("\nGrade Distribution:")
for letter, count in distribution.items():
    print(letter, ":", count)
