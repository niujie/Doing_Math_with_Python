'''
Use gradient descent to find the minimum value of a
single-variable function. This also checks for the existence
of a solution for the equation f'(x) = 0.
'''

from sympy import Derivative, Symbol, sympify, solve, plot
from sympy.core.sympify import SympifyError
from sympy.plotting.plot import List2DSeries
import numpy as np
import matplotlib.pyplot as plt
import sympy

def grad_descent(x0, f1x, x):
    # Check if f1x=0 has a solution
    if not solve(f1x):
        print(f'Cannot continue, solution for {f1x} does not exist')
        return
    
    epsilon = 1e-6
    step_size = 1e-3
    x_old = x0
    x_new = x_old - step_size * f1x.subs({x: x_old}).evalf()
    x_list = [x_new]
    while abs(x_new - x_old) > epsilon:
        x_old = x_new
        x_new = x_old - step_size * f1x.subs({x: x_old}).evalf()
        x_list.append(x_new)
    
    return x_new, x_list

if __name__ == "__main__":
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable to differentiate with respect to: ')
    var0 = float(input('Enter the initial value of the variable: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_min, var_list = grad_descent(var0, d, var)
        if var_min:
            print(f'{var.name}: {var_min}')
            print(f'Minimum value: {f.subs({var: var_min})}')
        
        x = np.linspace(-2, 2, 100)
        fun = sympy.lambdify(var, f, "numpy")
        plt.plot(x, fun(x), 'b-', np.array(var_list), fun(np.array(var_list)), 'ro')
        plt.show()