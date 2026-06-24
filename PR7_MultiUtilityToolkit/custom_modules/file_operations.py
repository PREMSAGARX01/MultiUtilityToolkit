def create_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "x") as file:
            pass

        print("File created successfully.")

    except FileExistsError:
        print("File already exists.")


def write_file():
    filename = input("Enter file name: ")

    try:
        data = input("Enter data to write: ")

        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully.")

    except Exception as e:
        print("Error:", e)


def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())

    except FileNotFoundError:
        print("File not found.")


def append_file():
    filename = input("Enter file name: ")

    try:
        data = input("Enter data to append: ")

        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully.")

    except Exception as e:
        print("Error:", e)


def file_menu():
    while True:
        print("\n===== FILE OPERATIONS =====")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")