def get_numbers():
    numbers = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    return numbers


def reverse(numbers, start, end):
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1


def rotate_list(numbers, k):
    n = len(numbers)

    if n == 0:
        return

    k = k % n

    # Step 1: Reverse the whole list
    reverse(numbers, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(numbers, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(numbers, k, n - 1)


def display_result(numbers):
    print("=" * 45)
    print("ROTATE LIST USING REVERSAL ALGORITHM".center(45))
    print("=" * 45)
    print(f"{'Rotated List':<18}: {numbers}")
    print("=" * 45)


def main():
    numbers = get_numbers()

    k = int(input("Enter rotation: "))

    rotate_list(numbers, k)

    display_result(numbers)


main()