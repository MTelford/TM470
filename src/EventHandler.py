import pygame
from UI import UI



class EventHandler:
    def __init__(self):
        self.ui = UI()

    def handle_event(self, event, sprite=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse click")
            pos = pygame.mouse.get_pos()
            if sprite is not None:
                sprite.set_x_pos(pos[0])
                sprite.set_y_pos(pos[1])
                self.ui.draw_card(sprite)


        if event.type == pygame.MOUSEMOTION:
            print("mouse moving")

        elif event.type == pygame.MOUSEBUTTONUP:
            # self.dragging = False
            print("mouse release")