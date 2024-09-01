import pygame

from Card import Card

class SpriteFactory:
    def __init__(self):
        self.community_cards = pygame.sprite.Group()
        self.player1_cards = pygame.sprite.Group()
        self.player2_cards = pygame.sprite.Group()
        self.player1_starting_cards = pygame.sprite.Group()
        self.player2_starting_cards = pygame.sprite.Group()


    def get_sprite_group(self, group):

       match group:
            case "community_cards":
                return self.community_cards
            case "player1_cards":
                return self.player1_cards
            case "player2_cards":
                return self.player2_cards
            case "player1_starting_cards":
                return self.player1_starting_cards
            case "player2_starting_cards":
                return self.player2_starting_cards

            case _:
                raise Exception("No sprite group under that name exists.")



