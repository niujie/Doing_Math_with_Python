'''
证明函数在某一点处的连续性
'''
from sympy import Symbol, sympify, Limit
from sympy.core.sympify import SympifyError

def check_continuity(f, var, var0):
    var = Symbol(var)
    limit_plus = Limit(f, var, var0, dir='+').doit()
    limit_minus = Limit(f, var, var0, dir='-').doit()
    if limit_plus == limit_minus and limit_plus == f.subs({var: var0}):
        print(f'{f} is continuous at {var0}')
    else:
        print(f'{f} is not continuous at {var0}')


if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    var0 = input('Enter the point to check the continuity at: ')

    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        check_continuity(f, var, var0)