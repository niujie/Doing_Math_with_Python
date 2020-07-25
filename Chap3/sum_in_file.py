# Find the sum of number stored in a file

def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s += float(line)
    print(f'Sum of the numbers: {s}')

if __name__ == '__main__':
    sum_data('./mydata.txt')