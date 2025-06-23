
# Base Class (parent class)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# Derived class (child class) - Student
class Student(Person):
    def __init__(self, name, age, gender, roll_no, grade):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Role: Student, Roll No: {self.roll_no}, Grade: {self.grade}")


# Derived class(child class ) 
class Teacher(Person):
    def __init__(self, name, age, gender, employee_id, subject):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Role: Teacher, Employee ID: {self.employee_id}, Subject: {self.subject}")


# Derived class (child class )
class Staff(Person):
    def __init__(self, name, age, gender, department, shift):
        super().__init__(name, age, gender)
        self.department = department
        self.shift = shift

    def display_info(self):
        super().display_info()
        print(f"Role: Staff, Department: {self.department}, Shift: {self.shift}")


# store data
people = []

# Add a person
def add_person():
    print("\n1. Add Student")
    print("2. Add Teacher")
    print("3. Add  Cleaning Staff")
    choice = input("Enter your choice: ")

    name = input("Enter your complete  name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
      
    if choice == "1":
        roll_no = int(input("Enter Roll No: "))
        grade = input("Enter Grade: ")
        people.append(Student(name, age, gender, roll_no, grade))
        print("==================== Stusent is  successfuly Add =================== ")
    elif choice == "2":
        employee_id = int(input("Enter Employee ID: "))
        subject = input("Enter Subject: ")
        people.append(Teacher(name, age, gender, employee_id, subject))
        print(" =================== Teacher is successfuly Add =================== ")
    elif choice == "3":
        department = input("Enter Department: ")
        shift = input("Enter Shift: ")
        people.append(Staff(name, age, gender, department, shift))
        print(" ===================  your  cleaning staff is  successfuly Add =================== ")
    else:
        print(" =================== Invalid choice! =================== ")

# Display all the  data
def display_all():
    print(" what would you like to display")
    print("1. Student")
    print("2.  Teacher")
    print("3.  Cleaning Staff")
    
    choice = input("Enter your choice: ")
    if choice not in ("1" , "2" , "3"):
        print("=================== invalid=================== ")

    ID=input("Enter ID :")
    if not people:
        print("/n no record to display")
        return
    print("  ====print all record==== ")

    for person in people:
        print("")
        person.display_all()

def del_person():
    print("\n1. Del Student")
    print("2. Del Teacher")
    print("3. Del Staff")
    choice = input("Enter your choice: ")

    name = input("Enter  your complete name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")

    found = False

    if choice == "1":
        roll_no = input("Enter Roll No: ")
        grade = input("Enter Grade: ")
        for person in people:
            if (
                type(person).__name__ == "Student" and
                person.name == name,
                person.age == age ,
                person.gender == gender,
                person.roll_no == roll_no,
                person.grade == grade
            ):
            
                people.remove(person)
                found = True
                print("Student removed.")
                break

    elif choice == "2":
        employee_id = input("Enter Employee ID: ")
        subject = input("Enter Subject: ")
        for person in people:
            if (
                type(person).__name__ == "Teacher" and
                person.name == name ,
                person.age == age ,
                person.gender == gender,
                #person.employee_id == employee_id ,
                person.subject == subject
            ):
                people.remove(person)
                found = True
                print("Teacher removed.")
                break

    elif choice == "3":
        department = input("Enter Department: ")
        shift = input("Enter Shift: ")
        for person in people:
            if (
                type(person).__name__ == "Staff" and
                person.name == name ,
                person.age == age ,
                person.gender == gender ,
                person.department == department,
                person.shift == shift
            ):
                people.remove(person)
                found = True
                print("Staff removed.")
                break

    else:
        print("Invalid choice!")

    if not found:
        print("Person not found.")

# Search for a person
def search_person():
    keyword = input("Enter name, roll number, or employee ID: ")
    found = False

    for person in people:
        try:
            name_match = keyword in person.name
        except AttributeError:
            name_match = False
            roll_match = False
            emp_match = False

        if type(person).__name__ == "Student":
            try:
                roll_match = keyword == person.roll_no
            except AttributeError:
                pass

        elif type(person).__name__ == "Teacher":
            try:
                emp_match = keyword == person.employee_id
            except AttributeError:
                pass

        if name_match or roll_match or emp_match:
            found = True
            person.display_info()

    if not found:
        print("No matching record found.")

# Main menu
def menu():
    while True:
        print("\n====== School Management System ======")
        print("1. Add Person")
        print("2. Display All People")
        print("3. Search Person")
        print("4. del Person")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_person()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_person()
        elif choice == "4":
            del_person()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
