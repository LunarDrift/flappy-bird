from time import sleep
import pygame
from sys import exit
import random
from constants import *

# Initialize Pygame and screen
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# SOUNDS
pygame.mixer.music.load(BG_MUSIC)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

pygame.mixer.set_num_channels(32)

flap_sound = pygame.mixer.Sound(FLAP_SOUND)
flap_sound.set_volume(0.1)
die_sound = pygame.mixer.Sound(DIE_SOUND)
die_sound.set_volume(0.1)
point_sound = pygame.mixer.Sound(POINT_SOUND)
point_sound.set_volume(0.1)

last_flap_time = 0

# Pipe Spawning Timer
create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500) # every 1.5 seconds


# IMAGES
BG = pygame.image.load("assets/flappybirdbg.png")
BIRD_IMG = pygame.image.load("assets/flappybird.png")
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (BIRD_WIDTH, BIRD_HEIGHT)).convert_alpha()
TOP_PIPE_IMG = pygame.image.load("assets/toppipe.png")
TOP_PIPE_IMG = pygame.transform.scale(TOP_PIPE_IMG, (PIPE_WIDTH, PIPE_HEIGHT)).convert_alpha()
BOTTOM_PIPE_IMG = pygame.image.load("assets/bottompipe.png")
BOTTOM_PIPE_IMG = pygame.transform.scale(BOTTOM_PIPE_IMG, (PIPE_WIDTH, PIPE_HEIGHT)).convert_alpha()


class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT)
        self.img = img


class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, PIPE_X, PIPE_Y, PIPE_WIDTH, PIPE_HEIGHT)
        self.img = img
        self.passed = False


# Game logic
bird = Bird(BIRD_IMG)
pipes = []
score = 0
game_over = False


def draw():
    # Draw background and bird
    screen.blit(BG, (0,0))
    screen.blit(BIRD_IMG, bird)

    # Draw pipe pairs
    for pipe in pipes:
        screen.blit(pipe.img, pipe)

    # Draw score
    text_font = pygame.font.SysFont("freesansbold", 40)
    score_str = str(int(score))
    score_render = text_font.render(score_str, True, "white")
    if not game_over:
        screen.blit(score_render, (10, 5))


def draw_final_score():
    # Set up text display messages
    over_str = "Game Over!"
    final_score_str = f"Final Score: {int(score)}"
    try_again_str = "Click to try again."

    # Choose font and size
    text_font = pygame.font.SysFont("freesansbold", 40)
    try_again_font = pygame.font.SysFont("freesansbold", 30)
    
    # Render text surfaces
    over_render = text_font.render(over_str, True, (155, 0, 0))
    final_score_render = text_font.render(final_score_str, True, "white")
    try_again_render = try_again_font.render(try_again_str, True, "white")
    # Blit text surfaces to screen
    screen.blit(over_render, (WINDOW_WIDTH / 2 - over_render.get_width() / 2, (WINDOW_HEIGHT / 2 - over_render.get_height() / 2) - 50))
    screen.blit(final_score_render, (WINDOW_WIDTH / 2 - final_score_render.get_width() / 2, (WINDOW_HEIGHT / 2 - final_score_render.get_height() / 2) + 10))
    screen.blit(try_again_render, (WINDOW_WIDTH / 2 - try_again_render.get_width() / 2, (WINDOW_HEIGHT / 2 - try_again_render.get_height() / 2) + 70))


def move():
    global BIRD_VELOCITY_Y, score, game_over
    BIRD_VELOCITY_Y += GRAVITY
    bird.y += BIRD_VELOCITY_Y

    if bird.top < 0:
        bird.top = 0
        die_sound.play()
        game_over = True
        return
    if bird.bottom > WINDOW_HEIGHT:
        bird.bottom = WINDOW_HEIGHT
        die_sound.play()
        game_over = True
        return



    for pipe in pipes:
        pipe.x += PIPE_VELOCITY_X

        if not pipe.passed and bird.x > pipe.x + pipe.width:
            score += 0.5
            pipe.passed = True
            point_sound.play()

        if bird.colliderect(pipe):
            game_over = True
            die_sound.play()
            return
        

    # Clean up old pipes
    while len(pipes) > 0 and pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)



def create_pipes():
    random_pipe_y = PIPE_Y - PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
    
    # Gap between pipes
    gap_y = WINDOW_HEIGHT / 4
    
    # Top pipe
    top_pipe = Pipe(TOP_PIPE_IMG)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)
    # Bottom pipe
    bottom_pipe = Pipe(BOTTOM_PIPE_IMG)
    bottom_pipe.y = top_pipe.y + top_pipe.height + gap_y
    pipes.append(bottom_pipe)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over:
            create_pipes()

        # Add keyboard/mouse input here
        if event.type == pygame.MOUSEBUTTONDOWN:
            BIRD_VELOCITY_Y = -6
            current_time = pygame.time.get_ticks()
            if current_time - last_flap_time >= FLAP_COOLDOWN:
                last_flap_time = current_time
                flap_sound.play()

                # Press space to restart game
                if game_over:
                    bird.y = BIRD_Y
                    pipes.clear()
                    score = 0
                    game_over = False
                    pygame.mixer.music.rewind()
                


    if not game_over:
        # Move pipes to the left
        move()

        draw()
        pygame.display.update()
        clock.tick(FPS)
    else:
        sleep(0.2) # small delay to avoid immediate restart
        draw()
        draw_final_score()
        pygame.display.update()
        clock.tick(FPS)