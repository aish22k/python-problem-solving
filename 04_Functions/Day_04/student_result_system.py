

def get_student_details(num_sub):
    marks = []
    student_name=input("Enter Name:")
    roll_no=int(input("Enter Roll No:"))
    for m in range(1, num_sub + 1):
        mark = int(input(f"Enter mark {m}: "))
        marks.append(mark)

    return marks,student_name,roll_no
                

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    return total, average, highest, lowest, grade

def display_result(name,roll_no,total, average, highest, lowest, grade ):
    print("="*34)
    print("STUDENT RESULT".center(34))
    print("="*34)
    print(f"{'Student name':<15}:{name}")
    print(f"{'roll_no':<15}:{roll_no}")
    print(f"{'Total Mark':<15}:{total}")
    print(f"{'Average mark':<15}:{average:.2f}")
    print(f"{'Lowest mark':<15}:{lowest}")
    print(f"{'Highest Mark':<15}:{highest}")
    print(f"{'Grade':<15}:{grade}")
    print("-"*34)


def main():

    num_sub = int(input("Enter number of subjects: "))

    marks,name,roll_no = get_student_details(num_sub)

    total, average, highest, lowest, grade = calculate_result(marks)

    display_result(name,roll_no,total, average, highest, lowest, grade)

main()