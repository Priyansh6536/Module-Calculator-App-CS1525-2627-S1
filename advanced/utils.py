def get_user_number() -> float|int:
    """Collects and returns the user's number after validating its input.

    :return: The user's chosen number.
    """
    while True:
        user_input = input("What number would you like to use for the calculation?\n")
        if user_input.isnumeric():
            user_input = float(user_input)
            return user_input
        else:
            print("Please enter a valid number")



def get_operation() -> str:
    """Collects and returns the user's operation after validating its input.

    :return: The user's chosen operation.
    """
    sign_list = ["+", "-", "*", "/"]
    while True:
        user_input = input("What operation would you like to do?\n")
        if user_input in sign_list:
            return user_input
        else:
            print("Please enter a valid operation from: +, -, *, /")



