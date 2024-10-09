usr_name = input("Enter the username: ")
if len(usr_name) >= 5 and usr_name.isalnum():
    print("Valid username.")
else:
    ("Invalid username.")