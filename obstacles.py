from random import randint
from random import seed, random
import pygame

"""Imports all the pygame modules and random modules"""

pygame.init()

size = width, height = 1300, 720
screen = pygame.display.set_mode(size)

"""Displays a basic window with width and height to work on"""


"""This class is for the cars that are moving"""

class car:

    def __init__(self, x_pos, y_pos):
        self.image = pygame.image.load(
            'car.png')
        self.image = pygame.transform.scale(self.image, (125, 100))
        self.x = x_pos
        self.y = y_pos
        self.hitbox = (self.x + 8, self.y + 18, 110, 110)

        """Defines postion and hitboxes"""

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x + 8, self.y + 18, 110, 39)

        """Blits the image and its image on the screen"""

    def update(self, speed):
        self.x = (self.x % 1250 + speed % 1250) % 1250

    """Function to move the Cars"""




"""This class is for the bushes that are not moving"""

class cactus:

    def __init__(self, x_pos, y_pos):
        self.image = pygame.image.load('cactus.png')
        self.image = pygame.transform.scale(self.image, (145, 85))
        self.x = x_pos
        self.y = y_pos
        self.hitbox = (self.x + 15, self.y, 115, 80)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x + 15, self.y, 115, 80)
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
