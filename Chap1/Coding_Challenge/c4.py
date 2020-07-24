'''
Fraction operations
'''
from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a + b))

def subtract(a, b):
    print('Result of Addition: {0}'.format(a - b))

def multiply(a, b):
    print('Result of Addition: {0}'.format(a * b))

def divide(a, b):
    print('Result of Addition: {0}'.format(a / b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
    if op == 'Add':
        add(a, b)

    if op == 'Subtract':
        subtract(a, b)
    
    if op == 'Multiply':
        multiply(a, b)
    
    if op == 'Divide':
        divide(a, b)