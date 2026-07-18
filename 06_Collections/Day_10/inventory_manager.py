def add_product(inventory):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    inventory[product] = quantity

    print("Product added successfully.")


def update_product(inventory):
    product = input("Enter product name: ")

    if product in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[product] = quantity
        print("Quantity updated.")
    else:
        print("Product not found.")


def search_product(inventory):
    product = input("Enter product name: ")

    if product in inventory:
        print(f"{product} : {inventory[product]}")
    else:
        print("Product not found.")


def remove_product(inventory):
    product = input("Enter product name: ")

    if product in inventory:
        inventory.pop(product)
        print("Product removed.")
    else:
        print("Product not found.")


def display_inventory(inventory):

    print("\n" + "=" * 40)
    print("INVENTORY".center(40))
    print("=" * 40)

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product, quantity in inventory.items():
            print(f"{product:<20}: {quantity}")

    print("=" * 40)


def main():
    inventory = {}

    while True:

        print("\n1. Add Product")
        print("2. Update Quantity")
        print("3. Search Product")
        print("4. Remove Product")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            update_product(inventory)

        elif choice == "3":
            search_product(inventory)

        elif choice == "4":
            remove_product(inventory)

        elif choice == "5":
            display_inventory(inventory)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


main()