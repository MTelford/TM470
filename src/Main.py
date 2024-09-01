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

player1 = Player()
player2 = Player()

dealer = Dealer(player1, player2)
dealer.give_players_starting_cards()


ui = UI(dealer)
ui.set_game_window_caption("Jack Change It")
ui.change_display_surface_color("GREEN")
ui.draw_starting_cards()

event_handler = EventHandler(ui)


while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked!")
            event_handler.handle_event(event, player1.get_player_cards()[0])

        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse released!")

    pygame.display.update()

