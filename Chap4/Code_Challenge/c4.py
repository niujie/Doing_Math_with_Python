'''
解单变量不等式
'''

from sympy import solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality
from sympy import Poly, Symbol, pprint, sin, cos, sympify

def solve_inequality(ineq_obj):
    x = Symbol('x')
    lhs = ineq_obj.lhs
    if lhs.is_polynomial():
        p = Poly(lhs, x)
        rel = ineq_obj.rel_op
        pprint(solve_poly_inequality(p, rel))
    
    elif lhs.is_rational_function():
        lhs = ineq_obj.lhs
        numer, denom = lhs.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        rel = ineq_obj.rel_op
        pprint(solve_rational_inequalities([[((p1, p2), rel)]]))

    else:    
        pprint(solve_univariate_inequality(ineq_obj, x, relational=False))

if __name__ == "__main__":
    expr = input('Enter the expression of the inequality: ')
    try:
        ineq_obj = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        solve_inequality(ineq_obj)