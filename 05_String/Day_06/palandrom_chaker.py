def check_palindrom(word):
    Is_palindrom=False
    word=word.lower()
    word=word.replace(" ","")

    if word[::-1] == word:
        Is_palindrom=True
    else:
        Is_palindrom=False

    return Is_palindrom

def main():
    word=input("Enter the word to check palindrom:")
    ans=check_palindrom(word)
    print("It is palindrom" if ans else "It is not Palindrom")

main()
