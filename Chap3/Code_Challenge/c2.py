'''
统计计算器
'''

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    
    return numbers

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N / 2
        m2 = (N / 2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    
    return median

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    
    return modes

def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []

    for num in numbers:
        diff.append(num - mean)
    
    return diff

def calculate_variance_std(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)

    std = (variance) ** 0.5

    return variance, std

if __name__ == "__main__":
    numbers = read_data('../mydata.txt')
    mean = calculate_mean(numbers)
    print(f'Mean is: {mean}')
    median = calculate_median(numbers)
    print(f'Median is: {median}')
    modes = calculate_mode(numbers)
    print('Modes are:')
    for mode in modes:
        print(mode)
    variance, std = calculate_variance_std(numbers)
    print(f'Variance is: {variance}, standard deviation is: {std}')

