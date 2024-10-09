while True:
    try:
        Radius = float(input("Radius: "))
        Area = 3.14159 * Radius * Radius
        if Radius > 0:
            print(f"Area: {Area:.2f} square units")
        else:
            print("Radius cannot be a negative value.")
    except:
        print("The program ended by entering other than float object.")
        break