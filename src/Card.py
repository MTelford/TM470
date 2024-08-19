import pygame


class Card(pygame.sprite.Sprite):

        def __init__(self, image_path, x, y):
            super().__init__()  # Initialize the Sprite superclass
            self.image = pygame.image.load(image_path)  # Load the image
            self.rect = self.image.get_rect()  # Get the rect of the image
            self.rect.topleft = (x, y)  # Position the sprite