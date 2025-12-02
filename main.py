import pygame
from sys import exit
from constants import *

# Initialize
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

game_state = "START"
score = 0



# Game Loop
while True:
    # 60 fps
    dt = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Handle keyboard/mouse input here


    # if game_state == "PLAYING":
    #     update_game(dt)


    
    # draw()