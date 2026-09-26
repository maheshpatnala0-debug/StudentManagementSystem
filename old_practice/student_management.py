import json

students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def add_student():
    student_id = len(students) + 1

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    course = input("Enter your course: ")

    students.append([student_id, name, age, course])

    save_students()

    print("Student added successfully")


def view_students():
    print("----- Student Details -----")

    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("------------------------")


def search_student():
    search_id = int(input("Enter student ID to search: "))

    found = False

    for student in students:
        if student[0] == search_id:
            print("----- Student Found -----")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])

            found = True
            break

    if found == False:
        print("Student not found")


def update_student():
    update_id = int(input("Enter student ID to update: "))

    found = False

    for student in students:
        if student[0] == update_id:

            new_age = int(input("Enter new age: "))
            new_course = input("Enter new course: ")

            student[2] = new_age
            student[3] = new_course

            save_students()

            print("Student updated successfully")

            found = True
            break

    if found == False:
        print("Student not found")

def delete_student():
    delete_id = int(input("Enter student ID to delete: "))

    found = False

    for student in students:
        if student[0] == delete_id:

            students.remove(student)
            save_students()

            print("Student deleted successfully")

            found = True
            break

    if found == False:
        print("Student not found")


load_students()


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")