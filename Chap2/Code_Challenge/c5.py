'''
探索斐波那契数列与黄金比例
'''

import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series =[a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    
    return series

def plot_ratio(n):
    series = fibo(n)
    ratio = []
    for i in range(len(series) - 1):
        ratio.append(series[i+1] / series[i])
    
    plt.plot(ratio)
    plt.xlabel('No.')
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers')
    plt.show()

if __name__ == '__main__':
    n = 100
    plot_ratio(n)