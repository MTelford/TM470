import pygame


class EventHandler:
    def __init__(self, ui):
        self.ui = ui
    # only handles cards right now
    def handle_event(self, event, card):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse click")
            if card is not None:
                self.ui.draw_card(card)

