def count_frequency(sentence):
    frequency = {}

    for ch in sentence:
        if ch == " ":
            continue

        ch = ch.lower()

        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


def find_first_non_repeating(sentence, frequency):
    for ch in sentence:
        if ch == " ":
            continue

        if frequency[ch.lower()] == 1:
            return ch

    return None


def display_result(sentence, result):
    print("=" * 40)
    print("FIRST NON-REPEATING CHARACTER".center(40))
    print("=" * 40)
    print(f"{'Input':<15}: {sentence}")

    if result:
        print(f"{'Result':<15}: {result}")
    else:
        print("No non-repeating character found.")

    print("=" * 40)


def main():
    sentence = input("Enter a string: ")

    frequency = count_frequency(sentence)

    result = find_first_non_repeating(sentence, frequency)

    display_result(sentence, result)


main()