from Dealer import Dealer
from Card import Card


class Deck:
    def __init__(self):
        CARDS_PNG_PATH = "resources/cards/2H.png"
        self.deck =      ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
                          "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
                          "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
                          "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
                          "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
                          "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
                          "AC", "AS", "AD", "AH"]
        self.test_sprite = Card(CARDS_PNG_PATH, 620, 320)
        self.card_count = 52

    def get_next_card(self):
        if self.deck:
            self.card_count-= 1
            return self.deck.pop()
        else:
            return None


    def add_card(self, card):
        self.deck.append(card)
        self.card_count += 1

    def get_deck(self):
        return self.deck

    def get_test_sprite(self):
        return self.test_sprite

    # def shuffle_deck (self):
    #
    #
    #     self.deck = self.
