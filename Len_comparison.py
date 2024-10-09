str_1 = input("Enter a sequence of characters in this string 1: ")
str_2 = input("Enter a sequence of characters in this string 2: ")
if len(str_1) > len(str_2):
    print("The length of string 1 is greater than length of string 2.")
elif len(str_1) < len(str_2):
    print("The length of string 2 is greater than length of string 1.")
elif len(str_1) == len(str_2):
    print("The length of string 1 is equal to length of string 2.")