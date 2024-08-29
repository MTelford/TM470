import sys
import pygame
from pygame.locals import *
from UI import UI
from Card import Card
from EventHandler import EventHandler

ui = UI()
ui.set_game_window_caption("Jack Change It")

# probably needs some call to update the screen in order for it to work
ui.set_screen_width(2560)
ui.set_screen_height(1440)

DISPLAYSURF = ui.get_display_surf()
DISPLAYSURF.fill(ui.GREEN)

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
#
# two_clubs = Card("2C")
# ui.draw_card("2C")

event_handler = EventHandler()

# Game loop

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        event_handler.handle_event(event, "2C")


    pygame.display.update()
