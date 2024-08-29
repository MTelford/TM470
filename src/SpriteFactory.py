import pygame

from Card import Card

class SpriteFactory:
    def __init__(self):
        self.sprite_group = pygame.sprite.Group()

    def create_card_sprite(self, card):
        card = Card(card)
        self.sprite_group.add(card)
        return card

    def get_sprite_group(self):
        return self.sprite_group

