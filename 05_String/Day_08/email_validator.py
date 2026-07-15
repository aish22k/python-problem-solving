def validate_email(email):
    is_valid = True
    
    if email.count("@") != 1:
        is_valid = False
   
    if " " in email:
        is_valid = False
     
    if email.startswith("@"):
        is_valid = False

    
    if email.endswith("."):
        is_valid = False

 
    at_index = email.find("@")
    dot_index = email.rfind(".")

    if dot_index < at_index:
        is_valid = False

    
    if dot_index == at_index + 1:
        is_valid = False

    return is_valid


def display_result(email, result):
    print("=" * 40)
    print("EMAIL VALIDATOR".center(40))
    print("=" * 40)
    print(f"{'Email':<12}: {email}")

    if result:
        print(f"{'Status':<12}: Valid Email ✅")
    else:
        print(f"{'Status':<12}: Invalid Email ❌")

    print("=" * 40)


def main():
    email = input("Enter your email: ")

    result = validate_email(email)

    display_result(email, result)


main()