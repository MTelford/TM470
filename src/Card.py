import pygame


class Card(pygame.sprite.Sprite):

        def __init__(self, image):
            super().__init__()  # Initialize the Sprite superclass
            self.PATH_TO_CARD_PNG_IMGs = "resources/cards/"
            self.image = pygame.image.load(self.PATH_TO_CARD_PNG_IMGs + image + ".png")  # Load the image
            self.rect = self.image.get_rect()  # Get the rect of the image


        def get_x_pos(self):
            return self.rect.x

        def get_y_pos(self):
            return self.rect.y

        def set_x_pos(self, x_pos):
            self.rect.x = x_pos

        def set_y_pos(self, y_pos):
            self.rect.y = y_pos

