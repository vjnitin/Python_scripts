while True:
    try:
        Mass = float(input("Mass: "))
        if Mass > 0:
            c = 3 * 10 ** 8
            Energy = Mass * c * c
            print("Energy: ", Energy, 'Joules')
        else:
            print("Mass cannot be a negative value.")
    except:
        print("The program ended by entering other than float object.")
        break