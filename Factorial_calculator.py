while True:
    print("Enter a positive integer or enter other than int object to quit.")
    try:
        usr_input = int(input("Enter an integer: "))
        factorial = 1
        i = 1
        if usr_input > 0:
            for i in range(1, usr_input + 1):
                factorial *= i
                i += 1
            print(factorial)
        else:
            print("Enter only the positive integer.")
    except:
        print("The program ended by entering other than int object.")
        break