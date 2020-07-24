'''
Example of drawing a horizontal bar chart
'''

import matplotlib.pyplot as plt

def create_bar_chart(data, labels, xlabel, ylabel, title):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3, ...]
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # Number of steps I walked during the past week
    steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    # Corresponding days
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels, 'Steps', 'Day', 'Number of steps walked')

    n = int(input('Enter the number of categories: '))
    exp_list = []
    labels = []
    for i in range(n):
        label = input('Enter category: ')
        labels.append(label)
        exp = float(input('Expenditure: '))
        exp_list.append(exp)
    create_bar_chart(exp_list, labels, 'Amount', 'Categories', 'Weekly expenditures')