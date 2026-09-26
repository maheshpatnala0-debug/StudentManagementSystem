from database import db
from mysql.connector import Error


# ================= ADD STUDENT =================

def add_student():

    while True:
        name = input("Enter your name: ")

        if name.strip() == "":
            print("Name cannot be empty")
        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters")
        else:
            break

    while True:
        try:
            age = int(input("Enter your age: "))

            if age <= 0:
                print("Age must be greater than 0")
            elif age > 100:
                print("Please enter a valid age")
            else:
                break

        except ValueError:
            print("Please enter a valid age")

    while True:
        gender = input("Enter your gender: ")

        if gender.strip() == "":
            print("Gender cannot be empty")
        elif not gender.replace(" ", "").isalpha():
            print("Please enter a valid gender")
        else:
            break

    while True:
        phone = input("Enter your phone number: ")

        if not phone.isdigit():
            print("Phone number should contain only digits")
        elif len(phone) != 10:
            print("Phone number must be exactly 10 digits")
        else:
            break

    while True:
        email = input("Enter your email: ")

        if email.strip() == "":
            print("Email cannot be empty")
        elif "@" not in email or "." not in email:
            print("Please enter a valid email")
        else:
            break

    while True:
        course = input("Enter your course: ")

        if course.strip() == "":
            print("Course cannot be empty")
        else:
            break

    while True:
        try:
            marks = float(input("Enter your marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
            else:
                break

        except ValueError:
            print("Please enter valid marks")

    cursor = None

    try:
        cursor = db.cursor()

        query = """
        INSERT INTO students
        (name, age, gender, phone, email, course, marks)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            age,
            gender,
            phone,
            email,
            course,
            marks
        )

        cursor.execute(query, values)
        db.commit()

        print("Student added successfully")

    except Error as e:
        print("Error adding student:", e)
        db.rollback()

    finally:
        if cursor:
            cursor.close()


# ================= VIEW STUDENTS =================

def view_students():

    cursor = None

    try:
        cursor = db.cursor()

        query = """
        SELECT id, name, age, gender, phone, email, course, marks
        FROM students
        """

        cursor.execute(query)

        students = cursor.fetchall()

        print("\n----- Student Details -----")

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:

                print("ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Gender:", student[3])
                print("Phone:", student[4])
                print("Email:", student[5])
                print("Course:", student[6])
                print("Marks:", student[7])
                print("------------------------")

    except Error as e:
        print("Error viewing students:", e)

    finally:
        if cursor:
            cursor.close()


# ================= SEARCH STUDENT =================

def search_student():

    try:
        search_id = int(
            input("Enter student ID to search: ")
        )

    except ValueError:
        print("Please enter a valid student ID")
        return

    cursor = None

    try:
        cursor = db.cursor()

        query = """
        SELECT id, name, age, gender, phone, email, course, marks
        FROM students
        WHERE id = %s
        """

        cursor.execute(query, (search_id,))

        student = cursor.fetchone()

        if student:

            print("\n----- Student Found -----")

            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Gender:", student[3])
            print("Phone:", student[4])
            print("Email:", student[5])
            print("Course:", student[6])
            print("Marks:", student[7])

        else:
            print("Student not found")

    except Error as e:
        print("Error searching student:", e)

    finally:
        if cursor:
            cursor.close()


# ================= UPDATE STUDENT =================

def update_student():

    try:
        update_id = int(
            input("Enter student ID to update: ")
        )

    except ValueError:
        print("Please enter a valid student ID")
        return

    while True:
        new_name = input("Enter new name: ")

        if new_name.strip() == "":
            print("Name cannot be empty")

        elif not new_name.replace(" ", "").isalpha():
            print("Name should contain only letters")

        else:
            break

    while True:
        try:
            new_age = int(
                input("Enter new age: ")
            )

            if new_age <= 0:
                print("Age must be greater than 0")

            elif new_age > 100:
                print("Please enter a valid age")

            else:
                break

        except ValueError:
            print("Please enter a valid age")

    while True:
        new_gender = input("Enter new gender: ")

        if new_gender.strip() == "":
            print("Gender cannot be empty")

        elif not new_gender.replace(" ", "").isalpha():
            print("Please enter a valid gender")

        else:
            break

    while True:
        new_phone = input("Enter new phone number: ")

        if not new_phone.isdigit():
            print("Phone number should contain only digits")

        elif len(new_phone) != 10:
            print("Phone number must be exactly 10 digits")

        else:
            break

    while True:
        new_email = input("Enter new email: ")

        if new_email.strip() == "":
            print("Email cannot be empty")

        elif "@" not in new_email or "." not in new_email:
            print("Please enter a valid email")

        else:
            break

    while True:
        new_course = input("Enter new course: ")

        if new_course.strip() == "":
            print("Course cannot be empty")

        else:
            break

    while True:
        try:
            new_marks = float(
                input("Enter new marks: ")
            )

            if new_marks < 0 or new_marks > 100:
                print("Marks must be between 0 and 100")

            else:
                break

        except ValueError:
            print("Please enter valid marks")

    cursor = None

    try:
        cursor = db.cursor()

        query = """
        UPDATE students
        SET name = %s,
            age = %s,
            gender = %s,
            phone = %s,
            email = %s,
            course = %s,
            marks = %s
        WHERE id = %s
        """

        values = (
            new_name,
            new_age,
            new_gender,
            new_phone,
            new_email,
            new_course,
            new_marks,
            update_id
        )

        cursor.execute(query, values)

        db.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully")

        else:
            print("Student not found")

    except Error as e:
        print("Error updating student:", e)
        db.rollback()

    finally:
        if cursor:
            cursor.close()


# ================= DELETE STUDENT =================

def delete_student():

    try:
        delete_id = int(
            input("Enter student ID to delete: ")
        )

    except ValueError:
        print("Please enter a valid student ID")
        return

    cursor = None

    try:
        cursor = db.cursor()

        query = """
        SELECT id, name, age, gender, phone, email, course, marks
        FROM students
        WHERE id = %s
        """

        cursor.execute(query, (delete_id,))

        student = cursor.fetchone()

        if student:

            print("\n----- Student Found -----")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Gender:", student[3])
            print("Phone:", student[4])
            print("Email:", student[5])
            print("Course:", student[6])
            print("Marks:", student[7])

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirm.lower() == "yes":

                query = """
                DELETE FROM students
                WHERE id = %s
                """

                cursor.execute(query, (delete_id,))

                db.commit()

                print("Student deleted successfully")

            else:
                print("Delete cancelled")

        else:
            print("Student not found")

    except Error as e:
        print("Error deleting student:", e)
        db.rollback()

    finally:
        if cursor:
            cursor.close()