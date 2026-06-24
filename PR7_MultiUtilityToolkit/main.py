from toolkit.datetime_utils import datetime_menu
from toolkit.math_utils import math_menu
from toolkit.random_utils import random_menu
from toolkit.uuid_utils import uuid_menu

from custom_modules.file_operations import file_menu
from custom_modules.conversion_utils import conversion_menu

import math
import random
import uuid
import datetime


def explore_module():
    module_name = input("Enter module name: ")

    modules = {
        "math": math,
        "random": random,
        "uuid": uuid,
        "datetime": datetime
    }

    if module_name in modules:
        print(dir(modules[module_name]))
    else:
        print("Module not supported.")


def main():
    while True:
        print("\n==============================")
        print("MULTI UTILITY TOOLKIT")
        print("==============================")
        print("1. Datetime Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. UUID Generator")
        print("5. File Operations")
        print("6. Unit Conversions")
        print("7. Explore Module (dir())")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            conversion_menu()

        elif choice == "7":
            explore_module()

        elif choice == "8":
            print("Thank you for using the toolkit.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()