'''
计算百分位数
'''

from c2 import calculate_median

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    
    return numbers

def p_quantile(numbers, p):
    n = len(numbers)
    i = n * p / 100 + 0.5
    i = i - 1
    if i.is_integer():
        return numbers[i]
    else:
        k = int(i)
        f = i - k
        return (1 - f) * numbers[k] + f * numbers[k+1]

if __name__ == '__main__':
    numbers = read_data('/Users/niujie/Documents/Python_Doing_Math_With_Python/Chap3/mydata.txt')
    numbers.sort()
    #p = int(input('Enter the p quantile:' ))
    p = 0
    p_q = p_quantile(numbers, p)
    print(f'{p} quantile is: {p_q}')
    median = calculate_median(numbers)
    print(f'Median is: {median}')