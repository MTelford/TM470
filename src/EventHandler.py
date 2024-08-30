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

        # if event.type == pygame.MOUSEMOTION:
        #     print("mouse moving")
        #
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     self.dragging = False
        #     print("mouse release")