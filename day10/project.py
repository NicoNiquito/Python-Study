# Calculator

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

num1 = int(input('What\'s the first number? '))
num2 = int(input('What\'s the second number? '))
for operation in operations:
    print(operation)
operation_symbol = input('Pick a operation from the lines above: ')
for operation in operations:
    if operation_symbol == operation:
        print(operations[operation](num1, num2))



