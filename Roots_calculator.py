while True:
    try:
        Coefficient_a = float(input("Coefficient a: "))
        Coefficient_b = float(input("Coefficient b: "))
        Coefficient_c = float(input("Coefficient c: "))
        Discriminant = ((Coefficient_b ** 2) - (4 * Coefficient_a * Coefficient_c)) ** (1 / 2)
        Root1 = (- Coefficient_b + Discriminant) / (2 * Coefficient_a)
        Root2 = (- Coefficient_b - Discriminant) / (2 * Coefficient_a)
        print(f"Roots: {Root1:.2f}, {Root2:.2f}")
    except:
        print("The program ended by entering the float object.")
        break