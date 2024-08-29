import sys
import pygame
from pygame.locals import *
from UI import UI
from SpriteFactory import SpriteFactory

ui = UI()
DISPLAYSURF = ui.get_display_surf()
DISPLAYSURF.fill(ui.GREEN)

sprite_factory = SpriteFactory()
two_hearts = sprite_factory.create_card_sprite("2H")
sprites = sprite_factory.get_sprite_group()
ui.draw_card(two_hearts, 960, 540)

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Game loop

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    sprites.draw(DISPLAYSURF)


    pygame.display.update()
