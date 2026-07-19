def get_numbers():
    numbers = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    target = int(input("Enter target sum: "))

    return numbers, target


def find_two_sum(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        current = numbers[i]
        complement = target - current

        if complement in seen:
            return seen[complement], i

        seen[current] = i

    return None


def display_result(numbers, target, result):
    print("=" * 45)
    print("TWO SUM".center(45))
    print("=" * 45)

    print(f"{'Numbers':<15}: {numbers}")
    print(f"{'Target':<15}: {target}")

    if result:
        i, j = result

        print("\nPair Found")
        print(f"Index 1 : {i}")
        print(f"Index 2 : {j}")
        print(f"Values  : {numbers[i]} + {numbers[j]} = {target}")
    else:
        print("\nNo pair found.")

    print("=" * 45)


def main():
    numbers, target = get_numbers()

    result = find_two_sum(numbers, target)

    display_result(numbers, target, result)


main()