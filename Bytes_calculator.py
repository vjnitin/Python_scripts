while True:
    print("Enter an integer to run the program or enter other than int object to quit")
    try:
        usr_input = int(input("Enter an integer: "))
        import math
        num_bytes = math.ceil((usr_input).bit_length() / 8)
        print("Number of bytes required for the integer to store: ", num_bytes)
        bin_num = bin(int(usr_input))[2:]
        print("Binary representation of the integer: ", bin_num)
    except:
        print("The program has ended by entering other than int object.")
        break