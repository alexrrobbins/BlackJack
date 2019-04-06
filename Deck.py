import random
from Ace import Ace

class Deck():

    def __init__(self):
        ace = Ace()
        self.cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,
        9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,ace,ace,ace,ace]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)
