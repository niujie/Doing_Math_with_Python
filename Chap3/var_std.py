'''
Find the variance and standard deviation of a list of numbers
'''

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # Calculate the mean
    mean = s / N

    return mean

def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []

    for num in numbers:
        diff.append(num - mean)
    
    return diff

def calculate_variance(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)

    return variance

if __name__ == "__main__":
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))

    from matplotlib import pyplot as plt
    donations.sort()
    plt.plot(donations, marker='o')
    plt.plot([calculate_mean(donations)] * len(donations))

    donations = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393, 396]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))

    plt.plot(donations, marker='o')
    plt.plot([calculate_mean(donations)] * len(donations))
    plt.legend(['Donations 1', 'Mean donation 1', 'Donations 2', 'Mean donation 2'])
    plt.show()