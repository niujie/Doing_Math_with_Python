'''
用其它CSV数据做实验
'''

import csv
import matplotlib.pyplot as plt
from c2 import calculate_mean, calculate_median, calculate_variance_std

def read_csv(filename):
    dates = []
    years = []
    values = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            dates.append(row[0])
            years.append(row[0][:4])
            values.append(float(row[1]))
    
    dates.sort()
    years.sort()
    values.sort()
    return dates, years, values


if __name__ == '__main__':
    dates, years, values = read_csv('./USA_SP_POP_TOTL.csv')
    mean = calculate_mean(values)
    median = calculate_median(values)
    var, std = calculate_variance_std(values)
    print(f'Mean = {mean}, Median = {median}, Var = {var}, Std = {std}')
    
    plt.plot(years, values)
    plt.xlabel('Date')
    plt.ylabel('Population')
    plt.show()