import random

from pygame.mouse import get_pos


class Deck:
    def __init__(self):
        self.game_cards =      ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
                          "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
                          "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
                          "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
                          "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
                          "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
                          "AC", "AS", "AD", "AH"]
        self.tracking_cards = ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
                          "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
                          "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
                          "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
                          "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
                          "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
                          "AC", "AS", "AD", "AH"]
        random.shuffle(self.game_cards)
        self.card_count = len(self.game_cards) - 1


    def get_next_card(self):
        if self.game_cards:
            return self.game_cards.pop()
        else:
            # take some action to get more cards, e.g., reshuffle
            return None

    def remove_card(self, card):
        # for some reason, 2 different cards are being passed in
        print(card)
        if card in self.cards:
            self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)
        self.card_count += 1

    def get_cards(self):
        return self.cards

    def lower_card_count_by_one(self):
        self.card_count -= 1

    def set_cards(self, shuffled_cards):
        self.cards = shuffled_cards
