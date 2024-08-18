import pygame


class Card(pygame.sprite.Sprite):

    def __init__(self, card_sprite):
        super().__init__()

        # initialises card from randomised game_deck into a usable game sprite
        self.image = pygame.image.load("card_sprites/" + card_sprite + ".png")
        self.rect = self.image.get_rect()
        self.card_value = card_sprite