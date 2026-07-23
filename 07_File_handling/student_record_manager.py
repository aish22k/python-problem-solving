def add_student():

    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))

    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    print("\nStudent added successfully!")


def view_students():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            print("=" * 45)
            print("STUDENT RECORDS".center(45))
            print("=" * 45)

            if len(students) == 0:
                print("No student records found.")

            else:
                for student in students:

                    name, marks = student.strip().split(",")

                    print(f"{'Name':<10}: {name}")
                    print(f"{'Marks':<10}: {marks}")
                    print("-" * 45)

    except FileNotFoundError:
        print("No records found. Please add students first.")


def display_menu():

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")


def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()