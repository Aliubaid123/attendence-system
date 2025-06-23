def run_teacher_portal():
    import time
    from datetime import datetime

    # Teacher credentials
    teacher_username = "teacher1"
    teacher_password = "teacher123"

    # Subjects assigned to teacher
    teacher_subjects = [
        {"Teacher": "teacher1", "CourseCode": "ICS101", "CourseName": "Intro to Programming", "Lecture": 5, "Quizzes": 2, "Assignments": 1},
        {"Teacher": "teacher1", "CourseCode": "FSc102", "CourseName": "Discrete Math", "Lecture": 4, "Quizzes": 1, "Assignments": 2}
    ]

    # Students data
    student_list = [
        {"RollNo": "ICS-101", "Name": "Ali Khan", "Courses": ["ICS101", "FSc102"]},
        {"RollNo": "FSc-102", "Name": "Sara Ahmed", "Courses": ["FSc102"]},
        {"RollNo": "Icom-201", "Name": "Usman Malik", "Courses": []}
    ]

    # Results data
    results_data = [
        {"CourseCode": "ICS101", "Level": 1, "Marks": {"ICS-101": 18}},
        {"CourseCode": "ICS101", "Level": 2, "Marks": {"ICS-101": 20}},
        {"CourseCode": "FSc102", "Level": 1, "Marks": {"ICS-101": 15, "FSc-102": 19}},
        {"CourseCode": "FSc102", "Level": 3, "Marks": {"ICS-101": 22}}
    ]

    attendance_records = []

    def teacher_login():
        print("\n==== TEACHER LOGIN ====")
        username = input("Username: ")
        password = input("Password: ")
        if username == teacher_username and password == teacher_password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials!\n")
            return False

    def get_valid_number_input(prompt, min_val, max_val):
        while True:
            try:
                choice = int(input(prompt))
                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def mark_attendance():
        print("\n==== ATTENDANCE MENU ====")
        for i, subj in enumerate(teacher_subjects):
            print(f"{i+1}. {subj['CourseCode']} - {subj['CourseName']}")
        choice = get_valid_number_input("Select subject: ", 1, len(teacher_subjects)) - 1
        course = teacher_subjects[choice]

        while True:
            print(f"\n--- {course['CourseCode']} - {course['CourseName']} ---")
            print("1. Mark Attendance")
            print("2. View Attendance")
            print("3. Back to Dashboard")
            sub_option = input("Select an option (1-3): ")

            if sub_option == '1':
                print(f"\nCourse Code   : {course['CourseCode']}")
                print(f"Course Name   : {course['CourseName']}")
                enrolled = [s for s in student_list if course['CourseCode'] in s['Courses']]
                print(f"Class Strength: {len(enrolled)}")
                print(f"Lecture No    : {course['Lecture']}")
                print(f"Quizzes       : {course['Quizzes']}")
                print(f"Assignments   : {course['Assignments']}")

                date = datetime.today().strftime('%Y-%m-%d')
                for student in enrolled:
                    status = input(f"{student['RollNo']} - {student['Name']} (P/A): ").strip().upper()
                    if status in ["P", "A"]:
                        attendance_records.append({
                            "RollNo": student['RollNo'],
                            "Course": course['CourseCode'],
                            "Date": date,
                            "Status": "Present" if status == "P" else "Absent"
                        })
                print("Attendance marked successfully!\n")

            elif sub_option == '2':
                print("\n==== VIEW ATTENDANCE RECORDS ====")
                found = False
                for record in attendance_records:
                    if record["Course"] == course["CourseCode"]:
                        print(f"{record['Date']} - {record['RollNo']} - {record['Status']}")
                        found = True
                if not found:
                    print("No attendance records found for this course.")
            elif sub_option == '3':
                break
            else:
                print("Invalid option. Try again.")

    def manage_results(view_only=False):
        print("\n==== RESULTS MENU ====")
        for i, subj in enumerate(teacher_subjects):
            print(f"{i+1}. {subj['CourseCode']} - {subj['CourseName']}")
        choice = get_valid_number_input("Select subject: ", 1, len(teacher_subjects)) - 1
        selected_course = teacher_subjects[choice]['CourseCode']

        level = get_valid_number_input("Enter level number (1-3): ", 1, 3)
        existing_record = next((r for r in results_data if r['CourseCode'] == selected_course and r['Level'] == level), None)
        enrolled_students = [s for s in student_list if selected_course in s['Courses']]

        if view_only:
            print(f"\nLevel {level} Results:")
            if existing_record:
                for roll, marks in existing_record['Marks'].items():
                    print(f"{roll}: {marks} marks")
            else:
                print("No results available for this level.")
        else:
            if existing_record:
                print("Existing result found. Updating...")
                for student in enrolled_students:
                    roll = student['RollNo']
                    try:
                        marks = int(input(f"{roll} - {student['Name']} : "))
                        existing_record['Marks'][roll] = marks
                    except ValueError:
                        print("Invalid input. Skipping.")
            else:
                print("No result found. Creating new entry...")
                new_record = {
                    "CourseCode": selected_course,
                    "Level": level,
                    "Marks": {}
                }
                for student in enrolled_students:
                    roll = student['RollNo']
                    try:
                        marks = int(input(f"{roll} - {student['Name']}: "))
                        new_record['Marks'][roll] = marks
                    except ValueError:
                        print("Invalid input. Skipping.")
                results_data.append(new_record)
            print("Results saved successfully.")

    while True:
        if not teacher_login():
            if input("Try again? (y/n): ").lower() != 'y':
                break
            continue

        session_start = time.time()

        while True:
            if time.time() - session_start > 3600:
                print("\nSession expired after 60 minutes. Logging out automatically.")
                return

            print("\n==== TEACHER DASHBOARD ====")
            print("1. Mark Attendance")
            print("2. View Results")
            print("3. Add/Update Results")
            print("4. Logout")
            option = input("Select an option (1-4): ")

            if option == '1':
                mark_attendance()
            elif option == '2':
                manage_results(view_only=True)
            elif option == '3':
                manage_results(view_only=False)
            elif option == '4':
                print("Logging out...\n")
                break
            else:
                print("Invalid option. Try again.")

# Run the portal
run_teacher_portal()
