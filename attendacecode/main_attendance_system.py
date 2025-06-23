def run_student_portal():
    import csv, os
    from datetime import datetime

    def initialize_files():
        data = {
            "students.csv": [
                ["Batch", "Degree", "RollNo", "Name", "Password"],
                ["2023", "BSCS", "CS-101", "Ali Khan", "ali123"],
                ["2023", "BSCS", "CS-102", "Sara Ahmed", "sara456"],
                ["2024", "BBA", "BBA-201", "Usman Malik", "usman789"]
            ],
            "attendance.csv": [
                ["RollNo", "Date", "Status", "Course"],
                ["CS-101", "2023-10-01", "Present", "CS101"],
                ["CS-101", "2023-10-02", "Present", "CS101"],
                ["CS-101", "2023-10-03", "Absent", "CS101"],
                ["CS-101", "2023-10-04", "Present", "CS102"],
                ["CS-101", "2023-11-15", "Present", "CS101"],
                ["CS-102", "2023-10-01", "Present", "CS101"],
                ["BBA-201", "2023-10-01", "Present", "MGT201"]
            ],
            "courses.csv": [
                ["RollNo", "CourseCode", "CourseName"],
                ["CS-101", "CS101", "Intro to Programming"],
                ["CS-101", "CS102", "Discrete Math"],
                ["CS-102", "CS101", "Intro to Programming"],
                ["BBA-201", "MGT201", "Principles of Management"]
            ],
            "grades.csv": [
                ["RollNo", "CourseCode", "Grade"],
                ["CS-101", "CS101", "A"],
                ["CS-101", "CS102", "B+"],
                ["CS-102", "CS101", "A-"],
                ["BBA-201", "MGT201", "B"]
            ],
            "fees.csv": [
                ["RollNo", "TotalFees", "Paid", "Due"],
                ["CS-101", "50000", "40000", "10000"],
                ["CS-102", "50000", "45000", "5000"],
                ["BBA-201", "45000", "45000", "0"]
            ]
        }
        for file, rows in data.items():
            with open(file, 'w', newline='') as f:
                csv.writer(f).writerows(rows)

    def student_login():
        print("\n==== STUDENT PORTAL ====")
        batch = input("Batch: ").strip()
        degree = input("Degree: ").strip().upper()
        roll_no = input("Roll Number: ").strip().upper()
        with open("students.csv") as f:
            for row in csv.DictReader(f):
                if (row["Batch"].strip() == batch and 
                    row["Degree"].strip().upper() == degree and 
                    row["RollNo"].strip().upper() == roll_no):
                    if input("Password: ").strip() == row["Password"].strip():
                        print(f"\nWelcome, {row['Name']}!")
                        return roll_no
                    print("Incorrect Password!")
                    return None
        print("Student not found!")
        return None

    def student_menu(roll_no):
        while True:
            print("\n==== STUDENT DASHBOARD ====")
            print("1. View Attendance")
            print("2. View Fees")
            print("3. View Grades")
            print("4. Courses Enrolled")
            print("5. Attendance Percentage (by Year)")
            print("6. Logout")
            choice = input("Choose (1-6): ")
            if choice == '1': view_attendance(roll_no)
            elif choice == '2': view_fees(roll_no)
            elif choice == '3': view_grades(roll_no)
            elif choice == '4': view_courses(roll_no)
            elif choice == '5': yearly_attendance(roll_no)
            elif choice == '6': break
            else: print("Invalid choice!")

    def view_attendance(roll_no):
        course = input("Course code (optional): ").strip().upper()
        date = input("Date YYYY-MM-DD (optional): ").strip()
        print("\n==== ATTENDANCE RECORDS ====")
        found = False
        with open("attendance.csv") as f:
            for row in csv.DictReader(f):
                if row["RollNo"].strip().upper() == roll_no:
                    if (not course or row["Course"].strip().upper() == course) and (not date or row["Date"].strip() == date):
                        print(f"{row['Date']} | {row['Course']} | {row['Status']}")
                        found = True
        if not found:
            print("No records found!")

    def view_fees(roll_no):
        print("\n==== FEE DETAILS ====")
        with open("fees.csv") as f:
            for row in csv.DictReader(f):
                if row["RollNo"].strip().upper() == roll_no:
                    print(f"Total: {row['TotalFees']}, Paid: {row['Paid']}, Due: {row['Due']}")
                    return
        print("No fee record found.")

    def view_grades(roll_no):
        print("\n==== GRADES ====")
        found = False
        with open("grades.csv") as f:
            for row in csv.DictReader(f):
                if row["RollNo"].strip().upper() == roll_no:
                    print(f"{row['CourseCode']} | Grade: {row['Grade']}")
                    found = True
        if not found:
            print("No grades found.")

    def view_courses(roll_no):
        print("\n==== ENROLLED COURSES ====")
        found = False
        with open("courses.csv") as f:
            for row in csv.DictReader(f):
                if row["RollNo"].strip().upper() == roll_no:
                    print(f"{row['CourseCode']} | {row['CourseName']}")
                    found = True
        if not found:
            print("No course records.")

    def yearly_attendance(roll_no):
        year = input("Enter year (YYYY): ").strip()
        print(f"\n==== ATTENDANCE DETAILS FOR {year} ====")
        present, total = 0, 0
        with open("attendance.csv") as f:
            for row in csv.DictReader(f):
                if row["RollNo"].strip().upper() == roll_no and row["Date"].startswith(year):
                    print(f"{row['Date']} | {row['Course']} | {row['Status']}")
                    total += 1
                    if row["Status"].strip().lower() == "present":
                        present += 1
        if total:
            print(f"\nTotal Classes: {total}, Present: {present}, Attendance: {present / total * 100:.2f}%")
        else:
            print("No attendance records found for this year.")

    # Main loop
    initialize_files()
    while True:
        roll = student_login()
        if roll:
            student_menu(roll)
        else:
            if input("Try again? (y/n): ").lower() != 'y':
                print("Exiting Student Portal...")
                break

if __name__ == "__main__":
    run_student_portal()  