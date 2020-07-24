'''
"偶数奇数自动售货机"
'''
def print_numbers(num):
    if num % 2 == 0:
        for i in range(2, 21, 2):
            print(i)
    else:
        for i in range(1, 21, 2):
            print(i)

if __name__ == '__main__':
    num = float(input('Enter a number: '))
    if num.is_integer():
        print_numbers(num)
    else:
        print('Please enter an integer.')