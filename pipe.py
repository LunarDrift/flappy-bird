import pygame
from constants import PIPE_X, PIPE_Y, PIPE_WIDTH, PIPE_HEIGHT


class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, PIPE_X, PIPE_Y, PIPE_WIDTH, PIPE_HEIGHT)
        self.img = img
        self.passed = False