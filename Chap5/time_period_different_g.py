from sympy import FiniteSet, pi

def time_period(length, g):

    T = 2 * pi * (length / g)**0.5
    return T

if __name__ == "__main__":
    L = FiniteSet(15, 18, 21, 22.5, 25)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print(f'{"Length(cm)":^15}{"Gravity(m/s^2)":^15}{"Time Period(s)":^15}')
    for elem in L * g_values:
        l = elem[0]
        g = elem[1]
        t = time_period(l/100, g)

        print(f'{float(l):^15}{float(g):^15}{float(t):^15.3f}')