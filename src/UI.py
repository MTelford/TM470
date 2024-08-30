from audioop import error

import pygame
from SpriteFactory import SpriteFactory
from Card import Card
from Deck import Deck


class UI:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 100, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.DISPLAY_SURF = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.FPS = 60
        self.frame_per_sec = pygame.time.Clock()
        self.ui_sprite_factory = SpriteFactory()
        self.ui_sprites = self.ui_sprite_factory.get_sprite_group()
        self.deck = Deck()
        self.screen_center_x = self.screen_height // 2
        self.screen_center_y = self.screen_width // 2


    def set_background(self, background):
        self.DISPLAY_SURF.fill(background)

    def set_display_surf(self):
        self.DISPLAY_SURF = pygame.display.set_mode((self.screen_width, self.screen_height))

    def get_display_surf(self):
        return self.DISPLAY_SURF

    def change_display_surface_color(self, color):
        if color == "GREEN":
            self.DISPLAY_SURF.fill(self.GREEN)
        elif color == "BLUE":
            self.DISPLAY_SURF.fill(self.BLUE)
        else:
            raise Exception("Invalid color passed to UI")
        pygame.display.flip()

    def set_screen_width(self, screen_width):
        self.screen_width = screen_width

    def set_screen_height(self, screen_height):
        self.screen_height = screen_height

    def get_screen_center(self):
        return self.screen_center_x, self.screen_center_y

    def set_game_window_caption(self, caption):
        pygame.display.set_caption(caption)

    def set_fps(self, fps):
        self.FPS = fps

    def draw_card(self, card):

        if card in self.deck.get_deck():

            temp_card = Card(card)
            # temp_card.rect.topleft = (temp_card.get_initial_x_pos(), temp_card.get_initial_y_pos())  # Position the sprite

            self.ui_sprites.add(temp_card)
            self.deck.remove_card(card)
            self.deck.lower_card_count_by_one()
            self.ui_sprites.draw(self.DISPLAY_SURF)
        else:
            print("Deck needs reshuffled")
