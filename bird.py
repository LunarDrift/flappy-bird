import pygame
from constants import BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT


class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT)
        self.img = img