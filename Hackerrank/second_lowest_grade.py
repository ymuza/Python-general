if __name__ == '__main__':
    # Create an empty list to store the student information
    students = []

    # Get the number of students from the user
    number_of_students = int(input())

    # Loop through number_of_students n times to get the name and grade for each student
    for _ in range(number_of_students):
        name = input()
        score = float(input())
        # Add the student's information as a list to the students list
        students.append([name, score])

    print(students)
    # Find the second lowest grade
    grades = sorted(set([student[1] for student in students]))
    second_lowest_grade = grades[1]

    # Get the names of the students with the second lowest grade
    names = sorted([student[0] for student in students if student[1] == second_lowest_grade])

    # Print the names
    for name in names:
        print(name)

