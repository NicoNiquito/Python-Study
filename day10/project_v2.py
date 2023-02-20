# Calculator

import art

# Adding

def add(n1, n2):
    return n1 + n2

# Subtract

def subtract(n1, n2):
    return n1 - n2

# Multiply

def multiply(n1, n2):
    return n1 * n2

# Divide

def divide(n1, n2):
    return n1 / n2

# Dictionary

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(art.logo)
    num1 = float(input('What\'s the first number? '))
    for operation in operations:
        print(operation)

    should_end = False

    while not should_end:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number? '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input('Type \'y\' to continue or something else to restart: ') == 'y':
            num1 = answer
        else:
            should_end = True
            calculator()   # This is called recursion
calculator()