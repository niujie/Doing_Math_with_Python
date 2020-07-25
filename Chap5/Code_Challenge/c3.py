'''
掷多少次硬币会输光你的钱？
'''
import random

def toss(money):
    n = 0
    while money > 0:
        n += 1
        if random.random() < 1/2:
            money += 1
        else:
            money -= 1.5
        print(f'Trails! Current amount: {money}')
    print(f'Game over: (Current amount: {money}. Coin tosses: {n}')

if __name__ == '__main__':
    money = float(input('Enter your starting amount: '))
    toss(money)