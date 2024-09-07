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
        self.ui_sprites = None
        self.screen_center = self.DISPLAY_SURF.get_rect().center
        self.STARTING_CARD_X_POS = [400, 500, 600, 700, 800, 900, 1000]
        self.STARTING_CARD_Y_POS = [900, 900, 900, 900, 900, 900, 900]
        self.first_card = True
        self.played_cards = []
        self.played_card_index = 0


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

    def set_game_window_caption(self, caption):
        pygame.display.set_caption(caption)

    def set_fps(self, fps):
        self.FPS = fps

    def update_display(self, sprite_card):

        self.ui_sprites.add(sprite_card)
        self.ui_sprites.draw(self.DISPLAY_SURF)
        pygame.display.flip()

    def draw_card(self, card, starting_cards=False, counter=0):

        print("drawing")
        sprite_card = Card(card)

        if starting_cards:
            sprite_card.set_x_pos(self.STARTING_CARD_X_POS[counter])
            sprite_card.set_y_pos(self.STARTING_CARD_Y_POS[counter])
            self.ui_sprites = self.ui_sprite_factory.get_sprite_group("player1_starting_cards")
            self.update_display(sprite_card)
        else:
            if self.first_card:
                screen_center_x = self.screen_center[0] - 25
                screen_center_y = self.screen_center[1] - 25
                self.first_card = False
            else:
                screen_center_x = self.screen_center[0]
                screen_center_y = self.screen_center[1]

            sprite_card.set_x_pos(screen_center_x)
            sprite_card.set_y_pos(screen_center_y)

            player1_cards = self.dealer.get_player1_cards()
            player2_cards = self.dealer.get_player2_cards()

            if card in player1_cards:
                self.dealer.player1.remove_card(card)
                print("removing from player 1")
                self.played_cards.append(card)
                self.ui_sprites = self.ui_sprite_factory.get_sprite_group("player1_cards")
                self.ui_sprite_factory.get_sprite_group("player1_starting_cards").empty()
                self.change_display_surface_color("GREEN")
                if not self.first_card:
                    played_card_sprite = Card(self.played_cards[self.played_card_index])
                    played_card_sprite.set_x_pos(self.screen_center[0] - 25)
                    played_card_sprite.set_y_pos(self.screen_center[1] - 25)
                    self.update_display(played_card_sprite)
                self.first_card = False 
                self.draw_starting_cards()
                self.update_display(sprite_card)
            elif card in player2_cards:
                self.dealer.player2.remove_card(card)
                print("removing from player 2")
                self.update_display(sprite_card)
            else:
                raise Exception("card not in either players cards")

    def draw_starting_cards(self):
        in_play_cards = self.dealer.get_player1_cards()
        counter = 0
        for card in in_play_cards:
            self.draw_card(card, True, counter)
            counter += 1

    def draw_played_card(self):
        self.draw_card(self.played_card)