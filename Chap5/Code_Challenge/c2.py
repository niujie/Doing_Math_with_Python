'''
大数定律
'''

import random

def roll(n):
    sum = 0
    for i in range(n):
        sum += random.randint(1, 6)
    print(f'Trials: {n} Trail average {sum / n}')

if __name__ == '__main__':
    e = sum([i / 6 for i in range(1, 7)])
    print(f'Expected value: {e}')
    N = [100, 1000, 10000, 100000, 500000]
    for n in N:
        roll(n)