def get_numbers():
    numbers = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    return numbers

def missing_num(numbers):
    num=len(numbers)+1
    total_sum=sum(numbers)
    expected_sum=(num*(num+1))//2
    final_ans=expected_sum-total_sum
    return final_ans



def display_result(ans):
    print("=" * 45)
    print("MISSING NUMBER".center(45))
    print("=" * 45)
    print(f"{'Missing Number':<18}: {ans}")
    print("=" * 45)


def main():
    numbers = get_numbers()

    ans=missing_num(numbers)

    display_result(ans)


main()