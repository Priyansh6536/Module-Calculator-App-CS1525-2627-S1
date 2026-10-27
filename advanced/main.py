import operations as op
import utils

number_1 = None
restart = True
while True:
    if restart:
        print("\nStep 1")
        number_1 = utils.get_user_number()
        print("\nStep 2")
        operation = utils.get_operation()
        print("\nStep 3")
        number_2 = utils.get_user_number()
        restart = False

    else:
        if operation == "+":
            print(f"Result: {op.add(number_1, number_2)}\n")
            restart = True
        elif operation == "-":
            print(f"Result: {op.subtract(number_1, number_2)}\n")
            restart = True
        elif operation == "*":
            print(f"Result: {op.multiply(number_1, number_2)}\n")
            restart = True
        elif operation == "/":
            if number_2 == (0):
                print("You cannot divide by 0")
                number_2 = utils.get_user_number()
            else:
                print(f"Result: {op.divide(number_1, number_2)}\n")
                restart = True