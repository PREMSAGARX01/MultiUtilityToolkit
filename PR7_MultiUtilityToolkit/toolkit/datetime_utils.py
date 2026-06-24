from datetime import datetime
import time


def show_current_datetime():
    now = datetime.now()
    print("\nCurrent Date and Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_date_difference():
    try:
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        diff = abs((d2 - d1).days)

        print(f"Difference: {diff} days")

    except ValueError:
        print("Invalid date format.")


def format_custom_date():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        print("Formatted Date:")
        print(date_obj.strftime("%d %B %Y"))

    except ValueError:
        print("Invalid date format.")


def stopwatch():
    input("Press ENTER to start stopwatch...")
    start = time.time()

    input("Press ENTER to stop stopwatch...")
    end = time.time()

    print(f"Elapsed Time: {end - start:.2f} seconds")


def countdown_timer():
    try:
        seconds = int(input("Enter countdown seconds: "))

        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

        print("Time's up!")

    except ValueError:
        print("Invalid input.")


def datetime_menu():
    while True:
        print("\n===== DATETIME MENU =====")
        print("1. Show Current Date & Time")
        print("2. Calculate Date Difference")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            show_current_datetime()

        elif choice == "2":
            calculate_date_difference()

        elif choice == "3":
            format_custom_date()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")