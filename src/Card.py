import pygame


class Card(pygame.sprite.Sprite):

        def __init__(self, image):
            super().__init__()  # Initialize the Sprite superclass
            self.PATH_TO_CARD_PNG_IMGs = "resources/cards/"
            self.image = pygame.image.load(self.PATH_TO_CARD_PNG_IMGs + image + ".png")  # Load the image
            self.rect = self.image.get_rect()  # Get the rect of the image
            self.initial_x_pos = 990
            self.initial_y_pos = 540
            self.x_pos = self.rect.x
            self.y_pos = self.rect.y

        def get_x_pos(self):
            return self.x_pos

        def get_y_pos(self):
            return self.y_pos

        def get_initial_x_pos(self):
            return self.initial_x_pos

        def get_initial_y_pos(self):
            return self.initial_y_pos

        def set_x_pos(self, x_pos):
            self.x_pos = x_pos

        def set_y_pos(self, y_pos):
            self.y_pos = y_pos

