import sys
import pygame
from pygame.locals import *
from src import Card, Dealer, Deck, Player, Scoreboard, UI, Sound, Networking
from collections import deque
import random

dealer = Dealer()
deck = Deck()
player = Player()
scoreboard = Scoreboard()
ui = UI()
sounds = Sound
networking = Networking()





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
    pygame.display.update()
