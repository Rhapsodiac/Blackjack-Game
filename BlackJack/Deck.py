from Card import Card
from random import *

class Deck(list):    
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    deckIndex = 0

    def __init__(self):
        self.init_deck()

    def init_deck(self):
          for c in range(2, 15):
              self.append(Card(val = c, suit = self.suits[0]))
          for c in range(2, 14):
              self.append(Card(val = c, suit = self.suits[1]))
          for c in range(2, 14):
              self.append(Card(val = c, suit = self.suits[2]))
          for c in range(2, 14):
              self.append(Card(val = c, suit = self.suits[3]))

    def randomize(self):
        shuffle(self)
        deckIndex = 0

    def get_card(self):
        new_card = self[self.deckIndex]
        if (self.deckIndex == 51):
            self.deckIndex = 0
        else:
            self.deckIndex += 1
        return new_card

    def get_deal(self):
        self.deckIndex = 0
        self.randomize()
        deal = [self.get_card(), self.get_card()]
        return deal

