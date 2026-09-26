# Student Management System

A Python and MySQL based Student Management System for managing student records efficiently.

## Features

* Add Student
* View Students
* Search Student
* Update Student
* Delete Student
* MySQL database integration
* Student data validation
* CRUD operations

## Technologies Used

* Python
* MySQL
* mysql-connector-python
* Git
* GitHub
* PyCharm

## Student Details

The system manages the following student information:

* Student ID
* Name
* Age
* Gender
* Phone
* Email
* Course
* Marks

## CRUD Operations

The project supports:

* **Create** – Add new student records
* **Read** – View and search student records
* **Update** – Modify existing student information
* **Delete** – Remove student records

## Project Structure

```text
StudentManagementSystem/
│
├── main.py
├── student.py
├── database.py
├── .gitignore
└── README.md
```

## How to Run

1. Install Python.
2. Install MySQL Server.
3. Create the required database and students table in MySQL.
4. Install the MySQL connector:

```bash
pip install mysql-connector-python
```

5. Update the MySQL connection details in `database.py`.
6. Run:

```bash
python main.py
```

## Author

**Mahesh**
