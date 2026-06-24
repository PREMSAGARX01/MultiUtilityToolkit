import math


def calculate_factorial():
    try:
        num = int(input("Enter a number: "))
        print("Factorial:", math.factorial(num))
    except ValueError:
        print("Invalid input.")


def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = float(input("Enter time (years): "))

        amount = principal * ((1 + rate / 100) ** years)

        print(f"Compound Interest Amount: {amount:.2f}")

    except ValueError:
        print("Invalid input.")


def trigonometry():
    try:
        angle = float(input("Enter angle in degrees: "))

        radians = math.radians(angle)

        print("sin =", round(math.sin(radians), 4))
        print("cos =", round(math.cos(radians), 4))
        print("tan =", round(math.tan(radians), 4))

    except ValueError:
        print("Invalid input.")


def area_calculator():
    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choose shape: ")

    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            area = math.pi * radius ** 2
            print(f"Area = {area:.2f}")

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"Area = {area:.2f}")

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"Area = {area:.2f}")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")


def math_menu():
    while True:
        print("\n===== MATH MENU =====")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area Calculator")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            calculate_factorial()

        elif choice == "2":
            compound_interest()

        elif choice == "3":
            trigonometry()

        elif choice == "4":
            area_calculator()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")