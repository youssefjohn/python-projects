from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(number1, number2, symbol):
    """Takes 2 numbers and a symbol, calculates,
    then prints the calculation and then returns"""
    calculation_symbol = operations[symbol]
    answer = calculation_symbol(number1, number2)
    return answer

def show_operators():
    """Prints the operators to the user"""
    for key in operations:
        print(key)



def calculation():
    """Runs main game. Makes the first calculation,
    then it enter a while loop to allow the user to keep calculating
    the first calculation, with a new calculation.
    """

    print(logo)
    num1 = round(float(input("Whats the first number? ")))
    show_operators()
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(float(input("Whats the second number? ")))
    first_answer = calculate(num1, num2, operation_symbol)
    print(first_answer)

    keep_playing = True
    while keep_playing:
        end_game = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation").lower()
        if end_game != 'y':
            keep_playing = False
            calculation()

        show_operators()
        next_number = round(float((input("What is the next number? "))))
        operation_symbol = input("Pick an operation: ")
        next_answer = calculate(first_answer, next_number, operation_symbol)
        print(next_answer)
        first_answer = next_answer


calculation()
