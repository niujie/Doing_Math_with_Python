'''
增强型乘法生成器
'''

def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter another number: ')
    multi_table(float(a), int(b))
