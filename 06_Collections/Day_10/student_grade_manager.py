def get_student_data():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"\nEnter student {i+1} name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks

    return students


def calculate_result(students):
    highest_student = max(students, key=students.get)
    lowest_student = min(students, key=students.get)

    average = sum(students.values()) / len(students)

    grades = {}

    for name, marks in students.items():

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "Fail"

        grades[name] = grade

    return highest_student, lowest_student, average, grades


def display_result(students, highest, lowest, average, grades):

    print("\n" + "=" * 45)
    print("STUDENT GRADE MANAGER".center(45))
    print("=" * 45)

    print(f"Highest Scorer : {highest} ({students[highest]})")
    print(f"Lowest Scorer  : {lowest} ({students[lowest]})")
    print(f"Average Marks  : {average:.2f}")

    print("\nStudent Grades")
    print("-" * 45)

    for name, grade in grades.items():
        print(f"{name:<15} {students[name]:<5} {grade}")

    print("=" * 45)


def main():
    students = get_student_data()

    highest, lowest, average, grades = calculate_result(students)

    display_result(students, highest, lowest, average, grades)


main()