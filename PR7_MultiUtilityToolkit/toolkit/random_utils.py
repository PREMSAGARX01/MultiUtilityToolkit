import random
import string


def random_number():
    try:
        start = int(input("Enter start value: "))
        end = int(input("Enter end value: "))

        print("Random Number:", random.randint(start, end))

    except ValueError:
        print("Invalid input.")


def random_list():
    try:
        size = int(input("Enter list size: "))

        numbers = [random.randint(1, 100) for _ in range(size)]

        print("Random List:")
        print(numbers)

    except ValueError:
        print("Invalid input.")


def random_password():
    try:
        length = int(input("Enter password length: "))

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        print("Generated Password:")
        print(password)

    except ValueError:
        print("Invalid input.")


def random_otp():
    otp = random.randint(100000, 999999)

    print("Generated OTP:", otp)


def random_menu():
    while True:
        print("\n===== RANDOM MENU =====")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Password")
        print("4. Generate OTP")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            random_number()

        elif choice == "2":
            random_list()

        elif choice == "3":
            random_password()

        elif choice == "4":
            random_otp()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")