def km_to_miles():
    try:
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371

        print(f"Miles: {miles:.2f}")

    except ValueError:
        print("Invalid input.")


def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter Celsius: "))

        fahrenheit = (celsius * 9 / 5) + 32

        print(f"Fahrenheit: {fahrenheit:.2f}")

    except ValueError:
        print("Invalid input.")


def conversion_menu():
    while True:
        print("\n===== CONVERSION MENU =====")
        print("1. KM to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            km_to_miles()

        elif choice == "2":
            celsius_to_fahrenheit()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")