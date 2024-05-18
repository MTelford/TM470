from collections import deque
import random
import pygame

card_deck = ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
             "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
             "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
             "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
             "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
             "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
             "AC", "AS", "AD", "AH"]


class Card(pygame.sprite.Sprite):

    def __init__(self, card_sprite):
        super().__init__()

        # initialises card from randomised game_deck into a usable game sprite
        self.image = pygame.image.load("card_sprites/" + card_sprite + ".png")
        self.rect = self.image.get_rect()
        self.card_value = card_sprite


class CardManager():
    """responsible for various card management features
        such as updating community card, giving players new cards etc"""

    def __init__(self, game_deck, DISPLAYSURF):
        self.game_deck = game_deck
        self.DISPLAYSURF = DISPLAYSURF
        self.community_card = None

    def get_next_card(self):
        # gets first card from shuffled deck
        return Card(self.game_deck.pop())

    def place_sprite(self, new_card, xpos, ypos):
        # positions new card
        new_card.rect.x = xpos
        new_card.rect.y = ypos

        # put card  onto the screen
        self.DISPLAYSURF.blit(new_card.image, new_card.rect)
        pygame.display.update()

    def update_community_card(self):
        # gets first card from shuffled deck and creates card object
        next_card = self.get_next_card()

        # keeps track of community card so as not to include in reshuffle 
        self.community_card = next_card.card_value

        # put card onto the screen
        self.place_sprite(next_card, 592, 283)

    def give_player_new_cards(self, amount=0):
        """ need to overlap cards every 20 pixels to make sure at least 50 fit on the top and bottom of the screen
            might need to do something like, put them all in the same place, if touching move it 20 pixels until
            nothing on the right hand side of the rect etc. """

        next_card = self.get_next_card()

        self.place_sprite(next_card, 5, 561)

        # here we check for overlaps and implement logic to neatly distribute cards on player screen at the bottom

        # if next_card.rect etc
