import pygame
from SpriteFactory import SpriteFactory
from Card import Card


class UI:
    def __init__(self, dealer):
        self.dealer = dealer
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
        self.screen_center_x = self.screen_height // 2
        self.screen_center_y = self.screen_width // 2
        self.STARTING_CARD_X_POS = [400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
        self.STARTING_CARD_Y_POS = [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900]


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

    def draw_card(self, card, starting_cards=False, counter=0):

        # don't need to check cards, just make sure to keep track of them
        print("drawing")
        sprite_card = Card(card)

        if starting_cards:
            sprite_card.set_x_pos(self.STARTING_CARD_X_POS[counter])
            sprite_card.set_y_pos(self.STARTING_CARD_Y_POS[counter])
        else:
            mouse_pos = pygame.mouse.get_pos()
            sprite_card.set_x_pos(mouse_pos[0])
            sprite_card.set_y_pos(mouse_pos[1])

            player1_cards = self.dealer.get_player1_cards()
            player2_cards = self.dealer.get_player2_cards()


            if card in player1_cards:
                self.dealer.player1.remove_card(card)
            elif card in player2_cards:
                self.dealer.player2.remove_card(card)
            else:
                raise Exception("card not in either players cards")

        self.ui_sprites.add(sprite_card)
        self.ui_sprites.draw(self.DISPLAY_SURF)
        pygame.display.flip()

    def draw_starting_cards(self):
        in_play_cards = self.dealer.get_in_play_cards()
        counter = 0
        for card in in_play_cards:
            self.draw_card(card, True, counter)
            counter += 1


