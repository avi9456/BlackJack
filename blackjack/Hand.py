# importing deck of card from Deck module
from blackjack import Deck
# hand class it define hands of player and dealer of the game
class Hand:
    # constructing player hand with zero card and total value 0 and also assigning if the player is dealer or not
    def __init__(self,dealer=False):
        self.hand = []
        self.value = 0
        self.dealer = dealer
    
    # adding card to player
    def add_card(self,card):
        self.hand.extend(card)

# calculating the value of player hand
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.hand:
            self.value += card.rank["value"]
            if card.rank["rank"] == "A":
                has_ace = True
            if has_ace and self.value > 21:
                self.value -= 10
    
    # get the calculated value
    def get_value(self):
        self.calculate_value()
        return self.value
    
    #checking if the player hit the blackjack, returning true or false accordingly 
    def is_blackjack(self):
        return self.get_value() == 21
    
    # displaying players card to player nad its value also
    # if the player is dealer then its hidde the first card and if the show_all_dealer_card set to true then only it show dealer all cards
    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's " if self.dealer else "Your "} hand:''')
        for index, card in enumerate(self.hand):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        
        if not self.dealer:
            print("Value: ",self.get_value())
        print()