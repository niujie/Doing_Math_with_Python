'''
Run until exit layout
'''

def fun():
    print('I am in an endless loop')

'''
Multiplication table printer with exit power to the user
'''

def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':
    while True:
        fun()
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
    
    while True:
        a = input('Enter a number: ')
        multi_table(float(a))

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break