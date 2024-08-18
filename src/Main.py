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

# set up random game deck and intialise card management component
# with card deck as deque for fast prepend/append

card_deck = ["2C", "2S", "2D", "2H", "3C", "3S", "3D", "3H",
             "4C", "4S", "4D", "4H", "5C", "5S", "5D", "5H",
             "6C", "6S", "6D", "6H", "7C", "7S", "7D", "7H",
             "8C", "8S", "8D", "8H", "9C", "9S", "9D", "9H",
             "10C", "10S", "10D", "10H", "JC", "JS", "JD", "JH",
             "QC", "QS", "QD", "QH", "KC", "KS", "KD", "KH",
             "AC", "AS", "AD", "AH"]

random.shuffle(card_deck)
# pass in DISPLAYSURF to update screen within card management class
card_management = CardManager(deque(card_deck), DISPLAYSURF)

card_management.give_player_new_cards()

# Game loop

while True:
    # Code
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
