


class Player:
    def __init__(self, name='', location=''):
        self.name = name
        self.location = location
        self.player_cards = []


    def get_name(self):
        return self.location

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    # def get_starting_cards(self):
    #     for i in range(0, 7):
    #         self.player_cards.append(self.dealer.get_next_card())

    def get_player_cards(self):
        return self.player_cards

    def set_player_cards(self, cards):
        self.player_cards = cards

    def remove_card(self, card):
        self.player_cards.remove(card)
