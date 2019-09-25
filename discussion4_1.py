while True:
    password = input("Please set the password: ")
    
    # requirement : minimum length 8
    if len(password) < 8:
        print("Invalid! The password should contain at least 8 digits. Try again.")
        continue
    # requirement : numbers and alphabetic letters 
    if not password.isalnum():
        print("Invalid! The password can only contain numbers and alphabetic letters. Try again.")
        continue
    # requirement : at least 1 capital letter 
    capitalValidity = False 
    for i in range(len(password)):
        if password[i].isupper:
            capitalValidity = True
            break
    if not capitalValidity:
        print("Invalid! The password must contain at least 1 captital letter. Try again.")
        continue
    
    print("The password is set successfully.")
    break

## if char in string.punctuation:
##    pass