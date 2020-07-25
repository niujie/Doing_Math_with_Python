'''
洗牌
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def create_deck():
    deck = []
    suits = ['spades', 'hearts', 'clubs', 'squares']
    ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for s in suits:
        for r in ranks:
            deck.append(Card(s, r))
    return deck

if __name__ == '__main__':
    deck = create_deck()
    print('before shuffle')
    print('-'*30)
    for card in deck:
        print(f'{card.rank} of {card.suit}')
    print('='*30)

    random.shuffle(deck)
    print('after shuffle')
    for card in deck:
        print(f'{card.rank} of {card.suit}')