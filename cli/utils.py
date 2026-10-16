def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def read_date(prompt):
    # MySQL validates the date format when the repository saves it.
    return input(prompt).strip()


def run_db_action(action, success_message):
    try:
        action()
        print(success_message)
    except Exception as error:
        print("Operation failed:", error)
