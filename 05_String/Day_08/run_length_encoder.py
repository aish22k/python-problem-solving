def compress_string(text):
    compressed = ""

    count = 1


    for i in range(len(text) - 1):

        if text[i] == text[i + 1]:
            count += 1

        else:
            compressed += text[i] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    return compressed


def display_result(original, compressed):
    print("=" * 40)
    print("RUN LENGTH ENCODER".center(40))
    print("=" * 40)
    print(f"{'Original':<12}: {original}")
    print(f"{'Compressed':<12}: {compressed}")
    print("=" * 40)


def main():
    text = input("Enter a string: ")

    compressed = compress_string(text)

    display_result(text, compressed)


main()