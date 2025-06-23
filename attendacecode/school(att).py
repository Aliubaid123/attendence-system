# parent class

class Person:
    def __init__(self, name, father_name):
        self.name = name
        self.father_name = father_name

# clild class (parent class :  person )
class Student(Person):
    def __init__(self, name, father_name):
        super().__init__(name, father_name)
        self.attendance = []  


#  Lists 
students = []  # List of Student 
attendance_log = []  # List of attandence log 


#  Functions
# add the student 

def add_student():
    
    name=input("\nEnter the complete  student name: ")
    if not name:
        print("❌ Student name cannot be empty.")
        return

    father = input("Enter the  father's name: ")
    if not father:
        print("❌ Father's name cannot be empty.")
        return

    for student in students:
        if student.name == name:
            print(" Student already exists.")
            return

    student = Student(name, father)
    students.append(student)
    print(f"✅ {name} Added successfully!\n")


# mark the attandence 
def mark_attendance():
    date = input("\nEnter date (DD-MM-YYYY): ")
    teacher = input("Enter teacher's name: ")
    records = []

    print("  Mark for  Attendance: P for  Present, A for  Absent, L for Leave, T for Late")
    for student  in students:
        while True:
            status = input(f"{student.name}: ")
            if status in ["P", "A", "L", "T"]:
                break
            print("Invalid input! Use P, A, L, or T.")
 
        # Store the  attendance  in attendence list 
        student.attendance.append((date, status))
        records.append((student.name, status))

        if status == "A":
            send_alert(student.name, date)

    attendance_log.append((date, teacher, records))
    print("Attendance marked successfully.\n")

#  function of alert message 

def send_alert(student_name, date):
    print(f"\nALERT: Message sent to {student_name}'s parents Absent on {date}")

# function of view attandence 
def view_attendance():
    date = input("\nEnter date (DD-MM-YYYY): ")
    found = False

    for record in attendance_log:
        if record[0] == date:
            found = True
            teacher = record[1]
            print(f" Attendance for {date} , Teacher: {teacher}")
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
        print("No attendance record found for that date.\n")


#  Main  function 

def  main():
 while True:
    print("\n==================== Attendance Management System ====================")
    print("Please choose an option:")
    print("1.  Add Student")
    print("2.  Mark Attendance")
    print("3.  View Attendance")
   # print("4' mark_attendance_by_class()")
    print("4.  Exit")


    choice = input("Enter your choice Between 1 and 4 : ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
        '''
    elif choice == "4":
        mark_attendance_by_class()'''
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
main()