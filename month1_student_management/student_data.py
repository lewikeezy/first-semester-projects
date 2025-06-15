students = []

def add_student():
    """
    Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    # getting user's input for student details
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    # Creating a dictionary to store a student's details
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    # Addding the "student" dictionary to the "students" list
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    """
    Print all the students in the list with their details.
    """
    #Looping through the students list to print each student's details 
    if len(students) == 0:
        print("No students have been added yet.\n")
    else:
        print("\nStudent List:")
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])
            print("-------------")

def get_average_grade():
    """
    Calculate and show the average grade of all students.
    """
    #  Checking if there are any students to calculate the average grade
    if len(students) == 0:
        print("No students to calculate average grade.\n")
    else:
        total = 0
        for student in students:
            total += student["grade"]

        average = total / len(students)
        print("Average Grade:", round(average, 2), "\n")
