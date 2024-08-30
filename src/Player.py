


class Player:
    def __init__(self, dealer, name='', location=''):
        self.name = name
        self.location = location
        self.player_cards = []
        self.dealer = dealer


    def get_name(self):
        return self.location

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def get_starting_cards(self):
        for i in range(0, 6):
            self.player_cards.append(self.dealer.get_next_card())

    def get_player_cards(self):
        return self.player_cards
