import random
from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()


    def get_deck(self):
        return self.deck

    def get_next_card(self, card):
        return self.deck.get_next_card()

    def shuffle_cards(self):
        current_cards = self.deck.get_cards()
        self.deck.set_cards(random.shuffle(current_cards))

    def request_card_removal(self, card):
        self.deck.remove_card(card)

