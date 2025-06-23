teachers = {}  # Global dictionary to store teacher login details

def admin():
    while True:
        print("\n  === Admin Panel ===  ")
        print("1. Add Teacher")
        print("2. View All Teachers")
        print("3. Exit Admin Panel")

        choice = input("Choose an option between 1 and 3: ")
        if choice == "1":
            username = input("Enter teacher's username: ")
            if username in teachers:
                print("❌ Username already exists.")
                continue

            password = input("Enter teacher's password: ")
            teachers[username] = password
            print(f"✅ Teacher '{username}' added successfully.\n")

        elif choice == "2":
            if not teachers:
                print("❌ No teachers added.")
            else:
                print("\n👩‍🏫 Registered Teachers:")
                for user in teachers:
                    print(f" - {user}")

        elif choice == "3":
            print("Exiting admin panel.")
            break
        else:
            print("❌ Invalid choice. Try again.")
