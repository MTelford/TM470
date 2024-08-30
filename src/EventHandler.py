import pygame
from UI import UI



class EventHandler:
    def __init__(self, ui):
        self.ui = ui
    # only handles cards right now
    def handle_event(self, event, sprite=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse click")
            if sprite is not None:
                self.ui.draw_card(sprite)

        # if event.type == pygame.MOUSEMOTION:
        #     print("mouse moving")
        #
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     self.dragging = False
        #     print("mouse release")