import sys
import random
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QIcon, QFont, QPalette, QColor, QBrush, QPixmap


class BlackJack:
    # Class variables
    # The deck of cards
    deck = []
    # The player's hand
    player_hand = []
    # The dealer's hand
    dealer_hand = []
    # The player's hand value
    player_hand_value = 0
    # The dealer's hand value
    dealer_hand_value = 0
    
    # The player's bet
    player_bet = 0
    # The player's bankroll
    player_bankroll = 0
    
    # The player's insurance bet
    player_insurance_bet = 0
    
    def __init__(self):
        # Initialize the deck
        self.decks = self.create_deck()
        
        # Initialize the player's hand
        self.player_hand = []
        self.skip = False
        # Initialize the dealer's hand
        self.dealer_hand = []
        # Initialize the player's hand value
        self.player_hand_value = 0
        # Initialize the dealer's hand value
        self.dealer_hand_value = 0
        
        # Initialize the player's bet
        self.player_bet = 0
        # Initialize the player's bankroll
        self.player_bankroll = 1000
        
        # Initialize the player's insurance bet
        self.player_insurance_bet = 0
        
    def create_deck(self):
        # Create the deck of cards
        deckz = []
        # Iterate through the suits
        for suit in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            # Iterate through the ranks
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                         "Jack", "Queen", "King"]:
                # Add the card to the deck
                deckz.append([suit, rank])
        # Return the deck
        return deckz
    def create_card(self, suit, rank):
        # Create a card
        card = [suit, rank]
        # Return the card
        return card
    def shuffle_deck(self):
        # Shuffle the deck
        random.shuffle(BlackJack.deck)
        
    def deal_cards(self, player, dealer, insurance):
        # Deal the cards
        # Check if the player is true
        if player and BlackJack.deck:
            # Deal the player's first card
            BlackJack.player_hand.append(BlackJack.deck.pop())
            # Deal the player's second card
            BlackJack.player_hand.append(BlackJack.deck.pop())
        # Check if the dealer is true and the deck is not empty
        if dealer and BlackJack.deck:
            # Deal the dealer's first card
            BlackJack.dealer_hand.append(BlackJack.deck.pop())
            # Deal the dealer's second card
            BlackJack.dealer_hand.append(BlackJack.deck.pop())
        # Check if the insurance is true and the deck is not empty
        if insurance and BlackJack.deck:
            # Deal the insurance card
            BlackJack.player_insurance_bet.append(BlackJack.deck.pop())
    
    def calculate_hand_value(self, hand):
        # Calculate the hand value
        hand_value = 0
        # Iterate through the cards in the hand
        for card in hand:
            # Check if the card is an ace
            if card[1] == "Ace":
                # Add 11 to the hand value
                hand_value += 11
                # Check if the hand value is greater than 21
                if hand_value > 21:
                    # Subtract 10 from the hand value
                    hand_value -= 10
            # Check if the card is a jack, queen, or king
            elif card[1] in ["Jack", "Queen", "King"]:
                # Add 10 to the hand value
                hand_value += 10
            # Check if the card is a 2, 3, 4, 5, 6, 7, 8, 9, or 10
            elif card[1] in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                # Add the rank to the hand value
                hand_value += int(card[1])
        # Return the hand value
        return hand_value
    
    
    def check_for_bust(self, hand_value):
        # Check if the hand value is greater than 21
        if hand_value > 21:
            # Return True
            return True
        # Return False
        return False
    
    def check_for_blackjack(self, hand_value):
        # Check if the hand value is equal to 21
        if hand_value == 21:
            # Return True
            return True
        # Return False
        return False
    
    def check_for_win(self, player_hand_value, dealer_hand_value):
        # Check if the player's hand value is greater than the dealer's hand value
        if player_hand_value > dealer_hand_value:
            # Return True
            return True
        # Return False
        return False
    
    def check_for_loss(self, player_hand_value, dealer_hand_value):
        # Check if the player's hand value is less than the dealer's hand value
        if player_hand_value < dealer_hand_value:
            # Return True
            return True
        # Return False
        return False
                    
                
        
                
        
        
        
        
class Mainwindow(QWidget):
    
    player_hand = []
    dealer_hand = []
    player_hand_value = 0
    dealer_hand_value = 0
    player_bet = 0
    player_bankroll = 1000
    player_insurance_bet = 0
    skip = False
    calculate_hand_value = BlackJack.calculate_hand_value(BlackJack, player_hand)
    create_card = BlackJack.create_card(BlackJack, "Spades", "Ace")
    
    deck = BlackJack.create_deck(BlackJack)
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("BlackJack")
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet("background-color: #222222;")
        
        self.create_widgets()
        self.create_layout()
        
        self.show()
        
    def create_widgets(self):
        self.label = QLabel("BlackJack", self)
        self.label.setStyleSheet("color: #ffffff; font-size: 24px;")
        
        self.button = QPushButton("Deal", self)
        self.button.setStyleSheet("background-color: #ffffff; color: #222222;")
        
        self.button.clicked.connect(self.deal_cards)
        
    def create_layout(self):
        self.quitbutton = QPushButton("Quit", self)
        self.quitbutton.setStyleSheet("background-color: #ffffff; color: #222222;")
        self.quitbutton.clicked.connect(self.close)
        self.hitbutton = QPushButton("Hit", self)
        self.hitbutton.setStyleSheet("background-color: #ffffff; color: #222222;")
        self.hitbutton.clicked.connect(self.hit)
        self.standbutton = QPushButton("Stand", self)
        self.standbutton.setStyleSheet("background-color: #ffffff; color: #222222;")
        self.standbutton.clicked.connect(self.stand)
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 0, 0, 1, 3)
        self.grid.addWidget(self.button, 1, 0, 1, 3)
        self.grid.addWidget(self.quitbutton, 2, 0, 1, 1)
        self.grid.addWidget(self.hitbutton, 2, 1, 1, 1)
        self.grid.addWidget(self.standbutton, 2, 2, 1, 1)
        self.setLayout(self.grid)
        
        
    def deal_cards(self):
        BlackJack.shuffle_deck(self)
        BlackJack.deal_cards(self, True, False, False)
        BlackJack.player_hand_value = BlackJack.calculate_hand_value(self, BlackJack.player_hand)
        self.label.setText(f"Your hand value is {BlackJack.player_hand_value}")
        self.button.setText("Next")
    
        
    def hit(self):
        BlackJack.deal_cards(self, True, False, False)
        BlackJack.player_hand_value = BlackJack.calculate_hand_value(self, BlackJack.player_hand)
        self.label.setText(f"Your hand value is {BlackJack.player_hand_value}")
        if BlackJack.check_for_bust(self, BlackJack.player_hand_value):
            self.label.setText(f"You busted with a hand value of {BlackJack.player_hand_value}")
            self.button.setText("Next")
        elif BlackJack.check_for_blackjack(self, BlackJack.player_hand_value):
            self.label.setText(f"You got a blackjack with a hand value of {BlackJack.player_hand_value}")
            self.button.setText("Next")

    def stand(self):
        BlackJack.skip = True
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec())