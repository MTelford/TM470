import random
from Deck import Deck


class Dealer:
    def __init__(self, player1, player2):
        self.deck = Deck()
        self.player1 = player1
        self.player2 = player2
        self.in_play_cards = self.give_players_starting_cards()


    def get_deck(self):
        return self.deck

    def get_next_card(self):
        return self.deck.get_next_card()

    def shuffle_cards(self):
        current_cards = self.deck.get_cards()
        self.deck.set_cards(random.shuffle(current_cards))

    def give_players_starting_cards(self):
        cards = []
        for i in range (0,14):
            card = self.deck.get_next_card()
            cards.append(card)
            self.deck.remove_card(card)
        self.player1.set_player_cards(cards[0:7])
        self.player2.set_player_cards(cards[7:14])
        return cards

    def get_player1_cards(self):
        return self.player1.get_player_cards()

    def get_player2_cards(self):
        return self.player2.get_player_cards()

    def get_in_play_cards(self):
        return self.in_play_cards
