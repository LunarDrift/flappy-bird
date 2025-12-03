import pygame
import random
from constants import *
from bird import Bird
from pipe import Pipe
from renderer import Renderer
from sound_manager import SoundManager


class Game:
    def __init__(self):
        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        # Renderer and SoundManager
        self.renderer = Renderer(self.screen)
        self.sounds = SoundManager()

        # Game state variables
        self.first_run = True

        # Load assets, sounds, overlay, timers, and reset game state
        self.init_assets()
        self.init_overlay()
        self.init_timers()
        self.reset_state()

    # ---------- Initialization Helpers ----------   
    def init_assets(self):
        # Load and scale images
        self.bg = pygame.image.load(BG_IMG)
        self.bird_img = pygame.transform.scale(pygame.image.load(BIRD_IMG), (BIRD_WIDTH, BIRD_HEIGHT)).convert_alpha()
        self.top_pipe_img = pygame.transform.scale(pygame.image.load(TOP_PIPE_IMG), (PIPE_WIDTH, PIPE_HEIGHT)).convert_alpha()
        self.bottom_pipe_img = pygame.transform.scale(pygame.image.load(BOTTOM_PIPE_IMG), (PIPE_WIDTH, PIPE_HEIGHT)).convert_alpha()

        # Create Bird
        self.bird = Bird(self.bird_img)


    def init_overlay(self):
        # Create overlay
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.overlay.set_alpha(128)  # Set transparency level (0-255)
        self.overlay.fill((30, 30, 30))  # Fill with dark gray color
        # Overlay font/text
        self.overlay_font = pygame.font.SysFont("pixeboy", 40)
        self.overlay_text = self.overlay_font.render("Click to Flap!", True, "white")
        self.overlay_text_rect = self.overlay_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    
    def init_timers(self):
        # Set up pipe spawn timer
        self.create_pipes_timer = pygame.USEREVENT + 0
        pygame.time.set_timer(self.create_pipes_timer, 1500)  # New pipes spawn every 1.5 seconds


    # ---------- Game State Management ----------
    def reset_state(self):
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.game_started = False
        self.bird_velocity_y = 0
        self.last_flap_time = 0
        self.bird.y = BIRD_Y

    
    # ---------- Event Handling ----------
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Spawn pipes only after game has started
            if event.type == self.create_pipes_timer and self.game_started and not self.game_over:
                self.create_pipes()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click()

    
    def handle_click(self):
        if not self.game_started:
            self.game_started = True
            # Get rid of first click delay on restarts
            if not self.first_run:
                self.flap()
            if self.first_run:
                self.first_run = False
        elif not self.game_over:
            self.flap()
        elif self.game_over:
            self.reset_state()
            self.sounds.rewind_music()

    
    def flap(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flap_time >= FLAP_COOLDOWN:
            self.last_flap_time = current_time
            self.bird_velocity_y = FLAP_STRENGTH
            self.sounds.play_flap()

    # ---------- Game Logic ----------
    def update(self):
        if not self.game_over:
            self.bird_velocity_y += GRAVITY
            self.bird.y += self.bird_velocity_y
            self.move_pipes()
            self.check_bounds()

    
    def move_pipes(self):
        for pipe in self.pipes:
            pipe.x += PIPE_VELOCITY_X
            if not pipe.passed and self.bird.x > pipe.x + pipe.width:
                self.score += 0.5
                pipe.passed = True
                self.sounds.play_point()
            if self.bird.colliderect(pipe):
                self.game_over = True
                self.sounds.play_die()
                return
        self.pipes = [pipe for pipe in self.pipes if pipe.x > -PIPE_WIDTH]

    
    def check_bounds(self):
        # Keep bird within vertical bounds and play die sound if out of bounds
        if self.bird.top < 0:
            self.bird.top = 0
            self.game_over = True
            self.sounds.play_die()
        if self.bird.bottom > WINDOW_HEIGHT:
            self.bird.bottom = WINDOW_HEIGHT
            self.game_over = True
            self.sounds.play_die()

    
    def create_pipes(self):
        random_pipe_y = PIPE_Y - PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        top_pipe = Pipe(self.top_pipe_img)
        top_pipe.y = random_pipe_y
        bottom_pipe = Pipe(self.bottom_pipe_img)
        bottom_pipe.y = top_pipe.y + PIPE_HEIGHT + PIPE_GAP
        self.pipes.extend([top_pipe, bottom_pipe])

    
    # ---------- Main Game Loop ----------
    def run(self):
        while True:
            self.handle_events()

            if not self.game_started and self.first_run:
                self.renderer.draw_game(self)
                self.renderer.draw_overlay(self.overlay, self.overlay_text, self.overlay_text_rect)
            else:
                self.update()
                self.renderer.draw_game(self)
                if self.game_over:
                    self.renderer.draw_final_score(self)

            pygame.display.update()
            self.clock.tick(FPS)