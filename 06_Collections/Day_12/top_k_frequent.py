def get_numbers():

    numbers = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    k = int(input("Enter K: "))

    return numbers, k


def top_k_frequent(numbers, k):
    frequency={}

    for num in numbers:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num] = 1
    
    sorted_frequency = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )
    result = []

    for i in range(k):
        result.append(sorted_frequency[i][0])

    return result

def display_result(result):

    print("=" * 45)
    print("TOP K FREQUENT ELEMENTS".center(45))
    print("=" * 45)

    print("Answer:")

    for num in result:
        print(num)

    print("=" * 45)


def main():

    numbers, k = get_numbers()

    result = top_k_frequent(numbers, k)

    display_result(result)


main()