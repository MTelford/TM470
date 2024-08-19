import sys
import pygame
from pygame.locals import *
from Card import Card
from collections import deque
import random

# dealer = Dealer()
# deck = Deck()
# player = Player()
# scoreboard = Scoreboard()
# ui = UI()
# sounds = Sound
# networking = Networking()





pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

DISPLAYSURF = pygame.display.set_mode((1280, 720))
DISPLAYSURF.fill(GREEN)
pygame.display.set_caption("Jack Change It")

CARDS_PNG_PATH = "resources/cards/2H.png"
test_sprite = Card(CARDS_PNG_PATH, 620, 320)
sprites = pygame.sprite.Group()
sprites.add(test_sprite)

# pass in DISPLAYSURF to update screen within card management class
# card_management = CardManager(deque(card_deck), DISPLAYSURF)
#
# card_management.give_player_new_cards()

# Game loop

while True:
    # Code
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    sprites.draw(DISPLAYSURF)

    pygame.display.update()
