import random

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
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

        [[self.cards.append(Card(suit,rank)) for rank in ranks]for suit in suits]
        

    def Shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number=1)->int:
        if len(self.cards) >= number:
            return [self.cards.pop() for i in range(number)]


class Hand:
    def __init__(self,dealer=False):
        self.hand = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self,card):
        self.hand.extend(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.hand:
            self.value += card.rank["value"]
            if card.rank["rank"] == "A":
                has_ace = True
            if has_ace and self.value > 21:
                self.value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
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


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("Enter many games you want to play"))
            except:
                print("You must enter a number")
        
        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.Shuffle()
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
            
            print("\n"+"*"*45)
            print(f"{game_number} of {games_to_play}")
            dealer_hand.display()
            player_hand.display()

            if self.check_winner(player_hand,dealer_hand):
                continue
            
            choice =""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("please choose 'Hit' or 'Stand' (or H/S)").lower()
                print()
                while choice not in ["h","s","hit","stand"]:
                    choice = input("please choose 'Hit' or 'Stand' (or H/S)").lower()
                    print()
                if choice in ["h","hit"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Player Value: ",player_hand_value)
            print("Dealer's Value: ",dealer_hand_value)

            if self.check_winner(player_hand, dealer_hand,game_over=True):
                print("Thank you for playing")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        player_hand_value = player_hand.get_value()
        dealer_hand_value = dealer_hand.get_value()
        if not game_over:
            if player_hand_value > 21:
                print("You are busted! Dealer's win :(")
                return True
            elif dealer_hand_value > 21:
                print("Dealer's busted! You win:)")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both have blackjack! Tie")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You win :)")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer's have blackjack! Dealer's win :(")
                return True
        else:
            if player_hand_value > dealer_hand_value:
                print("You win :)")
            elif player_hand_value <dealer_hand_value:
                print("Dealer's win :(")
            else:
                print("Tie!")
            return True
        return False


G = Game()
G.play()