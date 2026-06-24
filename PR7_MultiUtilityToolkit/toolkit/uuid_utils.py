import uuid


def generate_uuid():
    unique_id = uuid.uuid4()

    print("\nGenerated UUID:")
    print(unique_id)


def uuid_menu():
    while True:
        print("\n===== UUID MENU =====")
        print("1. Generate UUID")
        print("2. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_uuid()

        elif choice == "2":
            break

        else:
            print("Invalid choice.")