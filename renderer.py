import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.SysFont("pixeboy", 50)
        self.font_small = pygame.font.SysFont("pixeboy", 40)
        self.font_score = pygame.font.SysFont("pixeboy", 60)

    
    def draw_game(self, game):
        """Draw background, bird, pipes, and score."""
        self.screen.blit(game.bg, (0, 0))
        self.screen.blit(game.bird.img, game.bird)
        for pipe in game.pipes:
            self.screen.blit(pipe.img, pipe)
        self.draw_score(game.score)

    
    def draw_score(self, score):
        """Draw current score on the screen."""
        score_surface = self.font_score.render(str(int(score)), True, "white")
        self.screen.blit(score_surface, (10, 5))

    
    def draw_overlay(self, overlay, overlay_text, overlay_rect):
        """Draw the dimmed overlay before the game starts."""
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(overlay_text, overlay_rect)

    def draw_final_score(self, game):
        """Draw the final score and game over text."""
        over_text = self.font_large.render("Game Over!", True, (155, 0, 0))
        final_score_text = self.font_large.render(f"Final Score: {int(game.score)}", True, "white")
        try_again_text = self.font_small.render("Click to try again.", True, "white")

        self.screen.blit(over_text, (WINDOW_WIDTH / 2 - over_text.get_width() / 2, (WINDOW_HEIGHT / 2 - over_text.get_height() / 2) - 50))
        self.screen.blit(final_score_text, (WINDOW_WIDTH / 2 - final_score_text.get_width() / 2, (WINDOW_HEIGHT / 2 - final_score_text.get_height() / 2) + 10))
        self.screen.blit(try_again_text, (WINDOW_WIDTH / 2 - try_again_text.get_width() / 2, (WINDOW_HEIGHT / 2 - try_again_text.get_height() / 2) + 70))