mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

def del_person():
    print("\n1. Add Student")
    print("2. Add Teacher")
    print("3. Add Staff")
    choice = input("Enter your choice: ")

    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")

    if choice == "1":
        roll_no = input("Enter Roll No: ")
        grade = input("Enter Grade: ")
        people.clear(Student(name, age, gender, roll_no, grade))
    elif choice == "2":
        employee_id = input("Enter Employee ID: ")
        subject = input("Enter Subject: ")
        people.clear(Teacher(name, age, gender, employee_id, subject))
    elif choice == "3":
        department = input("Enter Department: ")
        shift = input("Enter Shift: ")
        people.clear(Staff(name, age, gender, department, shift))
    else:
        print("Invalid choice!")





















        from admin_school_att import teachers  #  importe 

# --- Teacher Login ---
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in teachers and teachers[username] == password:
        print(" Login successful.")
        return True
    else:
        print(" Invalid username or password.\n")
        return False

# teacher login reqired before use the sysyem 
'''def initial_login():
    print("\n Teacher Login Required Before Using System")
    while True:
        if login():
            break
        else:
            retry = input("Do you want to try again? (yes / no ): ")
            if retry != 'yes':
                print(" Exit the  system  Goodbye!")
                exit()'''
import sys

def initial_login():
    print("\n Teacher Login Required Before Using System")
    while True:
        if login():
            break
        else:
            retry = input("Do you want to try again? (yes / no ): ").lower().strip()
            if retry != "yes":
                print(" Exit the system. Goodbye!")
                sys.exit()


# --- Student Class ---
class Person:
    def __init__(self, name, father_name):
        self.name = name
        self.father_name = father_name

class Student(Person):
    def __init__(self, name, father_name):
        super().__init__(name, father_name)
        self.attendance = []

# --- Global Lists ---
students = []
attendance_log = []

# --- Add Student ---
def add_student():
    name = input("\n Enter student name: ")
    if not name:
        print(" Student name cannot be empty.")
        return

    father = input("Enter father's name: ")
    if not father:
        print(" Father's name cannot be empty.")
        return

    for student in students:
        if student.name == name:
            print(" Student already exists.")
            return

    student = Student(name, father)
    students.append(student)
    print(f" {name} added successfully.\n")

# --- Mark the  Attendance ---
def mark_attendance():
    date = input("\nEnter date (DD-MM-YYYY): ")
    teacher = input("Enter your (teacher's) name: ")
    records = []

    print("Mark Attendance (P = Present, A = Absent, L = Leave, T = Late):")
    for student in students:
        while True:
            status = input(f"{student.name}: ")
            if status in ["P", "A", "L", "T"]:
                break
            print(" Invalid input!  only use this  P, A, L, or T.")
        
        student.attendance.append((date, status))
        records.append((student.name, status))

        if status == "A":
            send_alert(student.name, date)

    attendance_log.append((date, teacher, records))
    print(" Attendance marked successfully.\n")


# --- Send Alert the  message to absent the student  ---
def send_alert(student_name, date):
    print(f" ALERT: Message sent to {student_name}'s parents (Absent on {date})")

# --- View Attendance of the teacher side ---
def view_attendance():
    date = input("\nEnter date (DD-MM-YYYY): ")
    found = False
    for record in attendance_log:
        if record[0] == date:
            found = True
            print(f"\n Attendance for {date} - Teacher: {record[1]}")
            for student_name, status in record[2]:
                full_status = {
                    "P": "Present",
                    "A": "Absent",
                    "L": "On Leave",
                    "T": "Late"
                }.get(status, "Unknown")
                print(f"{student_name}: {full_status}")
            break

    if not found:
        print(" No attendance record found for that date.")

# --- Main Menu ---
def main():
    while True:
        print("\n==================== Attendance Management System ====================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter your choice between 1 and 4: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_attendance()

        elif choice == "4":
            print(" Exiting. Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

# --- Run Program ---
if __name__ == "__main__":
    
    initial_login()  # this is for login first
    main()           # Then open menu
