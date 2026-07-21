def get_words():
    n = int(input("Enter number of words: "))

    words = []

    for i in range(n):
        word = input(f"Enter word {i+1}: ")
        words.append(word)

    return words
def group_anagrams(words):

    groups = {}

    for word in words:

        key = tuple(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return groups


def display_result(groups):

    print("=" * 45)
    print("GROUP ANAGRAMS".center(45))
    print("=" * 45)

    count = 1

    for group in groups.values():
        print(f"Group {count} : {group}")
        count += 1

    print("=" * 45)


def main():

    words = get_words()

    groups = group_anagrams(words)

    display_result(groups)


main()