'''
寻找因子
'''

from sympy import sympify, factor, pprint, SympifyError

if __name__ == '__main__':
    expr = input('Enter the expression: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        pprint(factor(expr))