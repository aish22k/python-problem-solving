
def strength_cheker(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    score=0

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower=True
        elif not ch.isalnum() and ch!=" ":
            has_special=True
            
    if len(password)>=8:
        score +=1
    else:
        print("pleas entr atleast 8 character password:")
    
    if has_special:
        score +=1

    if has_digit:
        score +=1
    
    if has_lower:
        score +=1
    
    if has_upper:
        score +=1

    return score , len(password),has_lower,has_upper,has_digit,has_special

def display_result(score,length,lower,upper, digit, special):
   
    if score>= 5:
        strength="Strong"
    elif score == 3 or score == 4:
        strength="Medium"
    else:
        strength="Weak"

    print("="*34)
    print("PASSWORD STRENGTH CHECKER".center(34))
    print("="*34)
    print(f"{'password length':<15}:{length}")
    print(f"{'Lowercase':<15}:{'Yes' if lower else 'No'}")
    print(f"{'Uppercase':<15}:{'Yes' if upper else 'No'}")
    print(f"{'Digit':<15}:{'Yes' if digit else 'No'}")
    print(f"{'Special case':<15}:{'Yes' if special else 'No'}")
    print("\n")
    print(f"{'strenght':<15}:{strength}")
   
    print("-"*34)

def main():
    password=input("Enter your password :")

    score,length,lower,upper,digit,special=strength_cheker(password)
    display_result(score,length,lower,upper,digit,special)

main()


