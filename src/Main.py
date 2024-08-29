import sys
import pygame
from pygame.locals import *
from UI import UI
from SpriteFactory import SpriteFactory

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

# Game loop

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # make the UI have access to the sprite factory so it can draw AND update the display surf, then just loop it from here

    ui.draw_card("2C", 500, 500)


    pygame.display.update()
