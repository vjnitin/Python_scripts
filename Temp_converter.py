while True:
    try:
        Temp = float(input("Enter the temperature: "))
        Temp_unit = input("If the temperature is Celsius enter 'c' or enter 'f' for Fahrenheit: ")
        if Temp_unit == "c":
            FHN = 9 / 5 * Temp + 32
            print(f"Fahrenheit: {FHN:.2f}°F")
        elif Temp_unit == "f":
            CEL = ((Temp - 32) * 5) / 9
            print(f"Celsius: {CEL:.2f}°C")
    except:
        print("The program ended by entering other than float object.")
        break