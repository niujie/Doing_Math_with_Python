'''
Roll a die until the total score is 20
'''

import matplotlib.pyplot as plt
import random

target_score = 20

def roll():
    return random.randint(1, 6)

if __name__ == '__main__':
    score = 0
    num_rolls = 0
    while score < target_score:
        die_roll = roll()
        num_rolls += 1
        print(f'Rolled: {die_roll}')
        score += die_roll
    
    print(f'Score of {score} reached in {num_rolls} rolls.')