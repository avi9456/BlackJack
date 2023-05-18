# card class
class Card:
    # init the card with suit and rank which is directory contaning rank and value
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    # __str__ return string in format "rank of suit", used to get the detail of card
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
