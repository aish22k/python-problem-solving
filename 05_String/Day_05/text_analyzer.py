
def sentence_analyser(sentence):
    vowel_count=0
    consonants_count=0
    digit_count=0
    space_count=0

    sentence_char=sentence.split()

    word_count= len(sentence_char)
    char_count=len(sentence)

    for ch in sentence:
        if ch.isdigit():
            digit_count +=1
        elif ch.isalpha():
            if ch.lower() in "aioue":
                vowel_count +=1
            else:
                consonants_count +=1
        elif ch==" ":
            space_count += 1

    return sentence, char_count,word_count,vowel_count,consonants_count,digit_count,space_count

def display_result(sentence,char_count,word_count,vowel_count,consonants_count,digit_count,space_count):

    print("="*34)
    print("TEXT ANALYZER".center(34))
    print("="*34)
    print(f"{'Sentence':<15}:{sentence}")
    print(f"{'Characters':<15}:{char_count}")
    print(f"{'Word':<15}:{word_count}")
    print(f"{'Vowel':<15}:{vowel_count}")
    print(f"{'Consonants':<15}:{consonants_count}")
    print(f"{'Digit':<15}:{digit_count}")
    print(f"{'Space':<15}:{space_count}")
   
    print("-"*34)

def main():
    sentence=input("Enter  yout sentence:")

    sentence,char_count,word_count,vowel_count,consonants_count,digit_count,space_count=sentence_analyser(sentence)
    display_result(sentence,char_count,word_count,vowel_count,consonants_count,digit_count,space_count)

main()
