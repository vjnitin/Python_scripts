while True:
    print("Enter a postive integer or enter other than int object to quit")
    try:
        usr_input = int(input("Enter an integer: "))
        if usr_input > 1:
            is_prime = True
            for i in range(2, usr_input):
                if usr_input % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("The number is prime.")
            else:
                print("The number is not prime.")
        else:
            if usr_input < 0:
                print("Enter only the positive integer.")
            else:
                print("The number is not prime.")
    except:
        print("The program ended by entering other than int object.")
        break