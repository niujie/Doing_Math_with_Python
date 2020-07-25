'''
级数求和
'''

from sympy import Symbol, sympify, summation, pprint

def sum_series(expr, n_val, x_value):
    x = Symbol('x')
    n = Symbol('n')
    s = summation(expr, (n, 1, n_val))
    pprint(s)

    series_value = s.subs({x: x_value})
    print(f'Value of the series at {x_value}: {series_value}')    

if __name__ == '__main__':
    expr = input('Enter the n-th expression of the series: ')
    n = int(input('Enter the number of terms in the series: '))
    x = float(input('Enter the value of x at which you want to evaluate the series: '))

    sum_series(expr,n, x)