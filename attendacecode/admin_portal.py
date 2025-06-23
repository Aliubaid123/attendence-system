# Admin data
admin_username = "admin"
admin_password = "admin123"

# Sample data
teachers = [
    {"username": "teacher1", "password": "pass123", "name": "Ali Khan"},
    {"username": "teacher2", "password": "haider456", "name": "Haider"}
]

students = [
    {"roll_no": "ICS-101", "name": "Sara Ahmed", "courses": ["ICS101", "FSc102"]},
    {"roll_no": "FSc-102", "name": "Ali Raza", "courses": ["FSc102", "Math101"]},
    {"roll_no": "icom-201", "name": "Usman Ali", "courses": ["Commerce101", "Accounting202"]}
]

courses = [
    {"code": "ICS101", "name": "Intro to Programming"},
    {"code": "FSc102", "name": "Discrete Math"},
    {"code": "Math101", "name": "Mathematics"},
    {"code": "Commerce101", "name": "Principles of Commerce"},
    {"code": "Accounting202", "name": "Advanced Accounting"}
]

results = [
    {"roll_no": "ICS-101", "course": "ICS101", "marks": 85},
    {"roll_no": "ICS-101", "course": "FSc102", "marks": 78},
    {"roll_no": "FSc-102", "course": "FSc102", "marks": 88},
    {"roll_no": "FSc-102", "course": "Math101", "marks": 75},
    {"roll_no": "icom-201", "course": "Commerce101", "marks": 80},
    {"roll_no": "icom-201", "course": "Accounting202", "marks": 90}
]

def admin_portal():
    def admin_login():
        print("\n===== ADMIN LOGIN =====")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == admin_username and password == admin_password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials.\n")
            return False

    def list_teachers():
        print("\n--- Teachers List ---")
        for i, t in enumerate(teachers, 1):
            print(f"{i}. Username: {t['username']}, Name: {t['name']}")

    def add_teacher():
        print("\n--- Add Teacher ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter teacher name: ")
        teachers.append({"username": username, "password": password, "name": name})
        print("Teacher added successfully.")

    def delete_teacher():
        list_teachers()
        try:
            idx = int(input("Enter number of teacher to delete: ")) - 1
            if 0 <= idx < len(teachers):
                removed = teachers.pop(idx)
                print(f"Teacher '{removed['username']}' deleted.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def list_students():
        print("\n--- Students List ---")
        for i, s in enumerate(students, 1):
            print(f"{i}. Roll No: {s['roll_no']}, Name: {s['name']}")

    def add_student():
        print("\n--- Add Student ---")
        roll_no = input("Enter roll number: ")
        name = input("Enter student name: ")
        courses_enrolled = input("Enter courses (comma separated): ").split(',')
        courses_enrolled = [c.strip() for c in courses_enrolled if c.strip()]
        students.append({"roll_no": roll_no, "name": name, "courses": courses_enrolled})
        print("Student added successfully.")

    def delete_student():
        list_students()
        try:
            idx = int(input("Enter number of student to delete: ")) - 1
            if 0 <= idx < len(students):
                removed = students.pop(idx)
                print(f"Student '{removed['roll_no']}' deleted.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def list_courses():
        print("\n--- Courses List ---")
        for i, c in enumerate(courses, 1):
            print(f"{i}. {c['code']} - {c['name']}")

    def add_course():
        print("\n--- Add Course ---")
        code = input("Enter course code: ")
        name = input("Enter course name: ")
        courses.append({"code": code, "name": name})
        print("Course added successfully.")

    def delete_course():
        list_courses()
        try:
            idx = int(input("Enter number of course to delete: ")) - 1
            if 0 <= idx < len(courses):
                removed = courses.pop(idx)
                print(f"Course '{removed['code']}' deleted.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def view_results():
        print("\n--- Student Results ---")
        if not results:
            print("No results available.")
            return
        for r in results:
            print(f"Roll No: {r['roll_no']}, Course: {r['course']}, Marks: {r['marks']}")

    # Admin login
    if not admin_login():
        return

    # Admin Panel Menu
    while True:
        print("\n==== ADMIN PANEL ====")
        print("1. Manage Teachers")
        print("2. Manage Students")
        print("3. Manage Courses")
        print("4. View Results")
        print("5. Logout")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            print("\n--- Manage Teachers ---")
            print("1. List Teachers")
            print("2. Add Teacher")
            print("3. Delete Teacher")
            sub_choice = input("Choose (1-3): ")
            if sub_choice == '1':
                list_teachers()
            elif sub_choice == '2':
                add_teacher()
            elif sub_choice == '3':
                delete_teacher()
            else:
                print("Invalid option.")

        elif choice == '2':
            print("\n--- Manage Students ---")
            print("1. List Students")
            print("2. Add Student")
            print("3. Delete Student")
            sub_choice = input("Choose (1-3): ")
            if sub_choice == '1':
                list_students()
            elif sub_choice == '2':
                add_student()
            elif sub_choice == '3':
                delete_student()
            else:
                print("Invalid option.")

        elif choice == '3':
            print("\n--- Manage Courses ---")
            print("1. List Courses")
            print("2. Add Course")
            print("3. Delete Course")
            sub_choice = input("Choose (1-3): ")
            if sub_choice == '1':
                list_courses()
            elif sub_choice == '2':
                add_course()
            elif sub_choice == '3':
                delete_course()
            else:
                print("Invalid option.")

        elif choice == '4':
            view_results()

        elif choice == '5':
            print("Logging out from Admin Portal.")
            break
        else:
            print("Invalid choice. Try again.")

# Run Admin Portal
admin_portal()
