'''
估计圆面积
'''

import random
from math import pi, sqrt

def distance(x, y, r):
    # center of the circle is (r, r)
    return sqrt((x-r)**2 + (y-r)**2);

def calculate_circle_area(r, n):
    M = 0;
    N = 0;
    for i in range(n):
        x = random.uniform(0, 2*r);
        y = random.uniform(0, 2*r);
        dist = distance(x, y, r);
        if dist > r:
            M += 1
        else:
            N += 1
    f = N / (N + M)
    estimated_area = f * (2*r)**2
    estimated_pi = 4 * f
    return estimated_area, estimated_pi

if __name__ == '__main__':
    N = [10**3, 10**5, 10**6]
    r = float(input('Radius: '))
    real_area = pi * r**2
    for n in N:
        estimated_area, estimated_pi = calculate_circle_area(r, n)
        print(f'Area: {real_area}, Estimated ({n} darts): {estimated_area}, {estimated_pi}')