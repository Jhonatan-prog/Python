import random

## shuffling cards
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(cards)
shuffle = input('shaffle cards (type Yes or Not): ').lower()

def shuffling(cards, shuffle):
    if shuffle == 'yes':
        random.shuffle(cards)
        print(cards)
        
shuffling(cards, shuffle)