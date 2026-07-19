def get_numbers():
    numbers = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    return numbers


def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates


def display_result(numbers, duplicates):
    print("=" * 40)
    print("DUPLICATE FINDER".center(40))
    print("=" * 40)

    print(f"{'Original List':<18}: {numbers}")

    print("\nDuplicate Numbers")

    if len(duplicates) == 0:
        print("No duplicates found.")
    else:
        for num in sorted(duplicates):
            print(num)

    print("=" * 40)


def main():
    numbers = get_numbers()

    duplicates = find_duplicates(numbers)

    display_result(numbers, duplicates)


main()