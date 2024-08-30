from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()


    def get_next_card(self, card):
        return self.deck.get_next_card()

    def shuffle_cards(self):
        import random
        random.shuffle(self.deck.get_deck())

    def request_card_removal(self, card):
        self.deck.remove_card(card)

    def get_deck(self):
        return self.deck

        # """responsible for various card management features
        #         such as updating community card, giving players new cards etc"""
        #
        # def __init__(self, game_deck, DISPLAYSURF):
        #     self.game_deck = game_deck
        #     self.DISPLAYSURF = DISPLAYSURF
        #     self.community_card = None
        #
        # def get_next_card(self):
        #     # gets first card from shuffled deck
        #     return Card(self.game_deck.pop())
        #
        # def place_sprite(self, new_card, xpos, ypos):
        #     # positions new card
        #     new_card.rect.x = xpos
        #     new_card.rect.y = ypos
        #
        #     # put card  onto the screen
        #     self.DISPLAYSURF.blit(new_card.image, new_card.rect)
        #     pygame.display.update()
        #
        # def update_community_card(self):
        #     # gets first card from shuffled deck and creates card object
        #     next_card = self.get_next_card()
        #
        #     # keeps track of community card so as not to include in reshuffle
        #     self.community_card = next_card.card_value
        #
        #     # put card onto the screen
        #     self.place_sprite(next_card, 592, 283)
        #
        # def give_player_new_cards(self, amount=0):
        #     """ need to overlap cards every 20 pixels to make sure at least 50 fit on the top and bottom of the screen
        #         might need to do something like, put them all in the same place, if touching move it 20 pixels until
        #         nothing on the right hand side of the rect etc. """
        #
        #     next_card = self.get_next_card()
        #
        #     self.place_sprite(next_card, 5, 561)
        #
        #     # here we check for overlaps and implement logic to neatly distribute cards on player screen at the bottom
        #
        #     # if next_card.rect etc



