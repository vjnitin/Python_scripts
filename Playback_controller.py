while True:
    print("Enter a string to run the program or enter 'q' to exit")
    original_string = input("user input: ")
    if original_string != 'q':
        original_string = original_string.replace(" "," ... ")
        print("output: ",original_string)
    else:
        print("The program ended by entering 'q'.")
        break