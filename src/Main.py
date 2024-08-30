import sys
import pygame
from pygame.locals import *
from UI import UI
from EventHandler import EventHandler
from Dealer import Dealer
from Player import Player

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

dealer = Dealer()

player = Player(dealer)
player.get_starting_cards()
card = player.get_player_cards()[0]

ui = UI(dealer)
ui.set_game_window_caption("Jack Change It")
ui.change_display_surface_color("GREEN")

event_handler = EventHandler(ui)


while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    event_handler.handle_event(event, "2C")
