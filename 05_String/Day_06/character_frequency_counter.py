def count_frequency(sentence):
    frequency = {}

    for ch in sentence:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


def display_result(frequency):
    print("=" * 40)
    print("CHARACTER FREQUENCY COUNTER".center(40))
    print("=" * 40)

    print(f"{'Character':<15}{'Frequency'}")
    print("-" * 40)

    for ch, count in frequency.items():
        if ch == " ":
            print(f"{'<space>':<15}{count}")
        else:
            print(f"{ch:<15}{count}")

    print("=" * 40)


def main():
    sentence = input("Enter a sentence: ")

    frequency = count_frequency(sentence)

    display_result(frequency)


main()