balance = int(input("Enter your Balance:"))

while True:
    print("=" * 35)
    print("ATM MENU".center(35))
    print("=" * 35)
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("=" * 35)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"\nCurrent Balance : ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current Balance : ₹{balance}")
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance : ₹{balance}")

    elif choice == 4:
        print("\nThank you for using our ATM.")
        break

    else:
        print("Invalid Choice! Please try again.")