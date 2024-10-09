while True:
    print("Enter a string to run the program or enter 'q' to exit")
    original_string = input("user input: ")
    altered_string = ""
    if original_string != 'q':
        for char in original_string:
            if ord(char) >= 65 and ord(char) <= 90:
                char = ord(char) + 32
            elif ord(char) >= 97 and ord(char) <= 122:
                char = ord(char) - 32
            else:
                char = ord(char)
            char_transform = chr(char)
            altered_string += char_transform 
        print("case altered:",altered_string)
    else:
        print("The program ended by entering 'q'.")
        break  