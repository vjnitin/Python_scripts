while True:
    a = "=" * 30    
    print(a, f"\nEnter a postive integer or enter other than int object to quit\n{a}")
    try:
        usr_input = int(input("Enter an integer: "))
        is_prime = True
        if usr_input > 1:
            for i in range(2, usr_input):
                if usr_input % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("The number is prime.")
            else:
                print("The number is not prime.")
        else:
            if usr_input >= 0:
                print("The number is not prime.")
            else:
                print("Enter only the positive integer.")
    except:
        print("The program ended by entering other than int object.")
        break
