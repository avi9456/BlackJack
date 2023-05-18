# importing hand, deck, and card class
from blackjack import Hand,Deck,Card
# game class it describe how the game is going to play
class Game:
    #  main play method
    def play(self):
        # number of game played and how many round the user want to play
        game_number = 0
        games_to_play = 0

# how many round user want to play 
        while games_to_play <= 0:
            try:
                games_to_play = int(input("Enter many games you want to play: "))
            except:
                print("You must enter a number")
        
        # it will play until game number not equal number of game to play
        while game_number < games_to_play:
            game_number += 1
            deck = Deck.Deck()
            deck.Shuffle()
            player_hand = Hand.Hand()
            dealer_hand = Hand.Hand(dealer=True)

            # giving two cards to player and dealer from shuffle deck of cards
            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
            
            print("\n"+"*"*45)
            print(f"{game_number} of {games_to_play}")
            # showing player nad dealer's card
            dealer_hand.display()
            player_hand.display()

            #  check the winner
            if self.check_winner(player_hand,dealer_hand):
                continue
            # palyer will choose if he want the hit or stand
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

# checking winner according different conditions
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