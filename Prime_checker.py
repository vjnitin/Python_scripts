while True:
    print("Enter a postive integer or enter other than int object to quit")
    try:
        usr_input = int(input("Enter an integer: "))
        if usr_input > 1:
            for i in range(2, usr_input):
                if usr_input % i == 0:
                    print("The number is not prime.")
                else:
                    print("The number is prime.")
        else:
            print("Enter only the positive integer.")
    except:
        print("The program ended by entering other than int object.")
        break
