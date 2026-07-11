def display_menu():
    print("=" * 35)
    print("PERSONAL EXPENSE MANAGER".center(35))
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. View Average Expense")
    print("4. View All Expenses")
    print("5. Exit")
    print("=" * 35)


def add_expense(expenses):
    amount = float(input("Enter expense amount: ₹"))

    if amount > 0:
        expenses.append(amount)
        print("Expense added successfully!")
    else:
        print("Invalid amount!")


def calculate_total(expenses):
    return sum(expenses)


def calculate_average(expenses):
    if len(expenses) == 0:
        return 0
    return sum(expenses) / len(expenses)


def view_expenses(expenses):
    if len(expenses) == 0:
        print("\nNo expenses added yet.")
        return

    print("\nYour Expenses")
    print("-" * 20)

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense:.2f}")


def main():
    expenses = []

    while True:
        display_menu()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense(expenses)

        elif choice == 2:
            total = calculate_total(expenses)
            print(f"\nTotal Expense : ₹{total:.2f}")

        elif choice == 3:
            average = calculate_average(expenses)
            print(f"\nAverage Expense : ₹{average:.2f}")

        elif choice == 4:
            view_expenses(expenses)

        elif choice == 5:
            print("\nThank you for using Personal Expense Manager.")
            break

        else:
            print("Invalid Choice! Please try again.")


main()