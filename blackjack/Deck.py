# importing Card class from blackjack module and random from standard package
from blackjack import Card
import random

# deck class, a deck contain collection of cards 
class Deck:
    # constructing all possible cards and storing it in a cards list
    def __init__(self):
        self.cards = []
        suits = ["hearts","spades","Clubs", "Diamonds"]
        ranks = [
            {"rank":"A","value":11},
            {"rank":"2","value":2},
            {"rank":"3","value":3},
            {"rank":"4","value":4},
            {"rank":"5","value":5},
            {"rank":"6","value":6},
            {"rank":"7","value":7},
            {"rank":"8","value":8},
            {"rank":"9","value":9},
            {"rank":"10","value":10},
            {"rank":"J","value":10},
            {"rank":"Q","value":10},
            {"rank":"K","value":10}
        ]

        # it is used in list compresion, but actually it is doing same as this
        #   for suit in suits:
        #         for rank in ranks:
        #             self.cards.append(Card.Card(suit,rank))
        [[self.cards.append(Card.Card(suit,rank)) for rank in ranks]for suit in suits]
        

# it is shuffleing the card to get card randomly not in any fixed order
    def Shuffle(self):
        if len(self.cards) > 1:#checking is there is only one card then don't shuffle
            random.shuffle(self.cards)

# it is used to distribute card to dealer and player by default it only give list of one card
    def deal(self, number=1)->int:
        if len(self.cards) >= number:
            return [self.cards.pop() for i in range(number)]