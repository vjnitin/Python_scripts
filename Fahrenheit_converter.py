while True:
    try:
        Celsius = float(input("Celsius: "))
        Fahrenheit = 9 / 5 * Celsius + 32
        print("Fahrenheit: ", Fahrenheit)
    except:
        print("The program ended by entering other than float object.")
        break