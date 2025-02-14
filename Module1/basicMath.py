# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 1: Critical Thinking Assignment
#
# To get familiar with Python programming and its related Integrated Development
# Environment (IDE), begin by writing a simple Python script with any desired functionality.
#
# This Python program will take two numbers from the user and perform the operation supplied by the user.
# Ask the user to input two numbers (num1 and num2).
# Ask the user to input the operation (+, -, *, /).
# Given those two numbers and the operation, perform the math function to find the output.
def add(first_number, second_number):
    print(first_number, "+", second_number, "is", first_number + second_number)


def subtract(first_number, second_number):
    print(first_number, "-", second_number, "is", first_number-second_number)


def multiply(first_number, second_number):
    print(first_number, "*", second_number, "is", first_number*second_number)


def divide(first_number, second_number):
    print(first_number, "/", second_number, "is", first_number/second_number)


def is_integer(my_input_value):
    try:
        int(my_input_value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    input_value = input('Input your first number: ')
    if is_integer(input_value):
        num1 = int(input_value)
        input_value = input('Input your second number: ')
        if is_integer(input_value):
            num2 = int(input_value)
            operation = str(input('Input the operation (+,-,*,/):'))

            if operation == "+":
                add(num1, num2)
            elif operation == "-":
                subtract(num1, num2)
            elif operation == "*":
                multiply(num1, num2)
            elif operation == "/":
                divide(num1, num2)
            else:
                print("This simple calculator doesn't perform this operation: ", operation)
        else:
            print("Input is not a valid number: ", input_value)
    else:
        print("Input is not a valid number: ", input_value)

