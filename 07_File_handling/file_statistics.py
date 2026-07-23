def get_file_name():

    file_name = input("Enter file name: ")

    return file_name


def file_statistics(file_name):

    with open(file_name, "r") as file:

        lines = file.readlines()

    line_count = len(lines)

    word_count = 0
    character_count = 0

    for line in lines:

        words = line.split()

        word_count += len(words)

        character_count += len(line)

    return line_count, word_count, character_count


def display_result(lines, words, characters):

    print("=" * 40)
    print("FILE STATISTICS".center(40))
    print("=" * 40)

    print(f"{'Lines':<15}: {lines}")
    print(f"{'Words':<15}: {words}")
    print(f"{'Characters':<15}: {characters}")

    print("=" * 40)


def main():

    file_name = get_file_name()

    lines, words, characters = file_statistics(file_name)

    display_result(lines, words, characters)


main()