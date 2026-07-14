def count_word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def display_result(frequency):
    print("=" * 40)
    print("WORD FREQUENCY COUNTER".center(40))
    print("=" * 40)
    print(f"{'Word':<20}{'Frequency'}")
    print("-" * 40)

    for word, count in frequency.items():
        print(f"{word:<20}{count}")

    print("=" * 40)


def main():
    sentence = input("Enter a sentence: ")

    frequency = count_word_frequency(sentence)

    display_result(frequency)


main()