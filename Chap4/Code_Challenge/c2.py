'''
图形方程求解器
'''

from sympy import Symbol, pprint, sympify, solve, SympifyError
from sympy.plotting import plot

def plot_expressions(expr1, expr2):
    p = plot(expr1, expr2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()

if __name__ == '__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        soln = solve((expr1, expr2))
        pprint(soln)
    
        plot_expressions(expr1, expr2)