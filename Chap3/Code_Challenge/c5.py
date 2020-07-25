'''
创建分组频数表
'''

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    # Width of each class
    width = (high - low) / n
    classes = []
    a = low
    b = low + width
    while a < (high - width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

def calculate_freq(numbers, classes):
    freq = {}
    for cl in classes:
        freq[cl] = 0
    for num in numbers:
        for cl in classes:
            if num >= cl[0] and num < cl[1]:
                freq[cl] += 1

    return freq

def read_data(file):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(float(line))
    
    return numbers

if __name__ == "__main__":
    numbers = read_data('/Users/niujie/Documents/Python_Doing_Math_With_Python/Chap3/Code_Challenge/data.txt')
    n = int(input('Enter the number of classes: '))
    classes = create_classes(numbers, n)
    freq = calculate_freq(numbers, classes)
    
    print('Grade\tFrequency')
    for k, v in freq.items():
        print(k, '\t', v)