import sys
import pygame
from pygame.locals import *
from UI import UI
from EventHandler import EventHandler

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

ui = UI()
ui.set_game_window_caption("Jack Change It")
ui.change_display_surface_color("GREEN")



while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
