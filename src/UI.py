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


    def set_background(self, background):
        self.DISPLAY_SURF.fill(background)

    def set_display_surf(self):
        self.DISPLAY_SURF = pygame.display.set_mode((self.screen_width, self.screen_height))

    def get_display_surf(self):
        return self.DISPLAY_SURF

    def change_display_surface_color(self, color):
        self.DISPLAY_SURF.fill(self.GREEN)

    def set_screen_width(self, screen_width):
        self.screen_width = screen_width

    def set_screen_height(self, screen_height):
        self.screen_height = screen_height

    def set_game_window_caption(self, caption):
        pygame.display.set_caption(caption)

    def set_fps(self, fps):
        self.FPS = fps

    def draw_card(self, card, x, y):
        if card in self.deck.get_deck():
            temp_card = Card(card)
            self.ui_sprites.add(temp_card)
            temp_card.rect.topleft = (x, y)  # Position the sprite
            self.deck.remove_card(card)
            self.deck.lower_card_count_by_one()
            self.ui_sprites.draw(self.DISPLAY_SURF)
        else:
            print("Deck needs reshuffled")
