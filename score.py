import pygame
from constants import ASTEROID_SCORES, SCREEN_HEIGHT, SCREEN_WIDTH


class Score:
    def __init__(self):
        self.score = 0

    def reset_score(self):
        self.score = 0

    def update_score(self, asteroid_radius):
        self.score += ASTEROID_SCORES[asteroid_radius]

    def draw(self, lifes, screen):
        font = pygame.font.SysFont("Arial", 24)

        text_surf = font.render(
            f"Lifes: {lifes}, Score: {self.score}", True, (255, 255, 255)
        )
        screen.blit(
            text_surf,
            (
                SCREEN_WIDTH - text_surf.get_width(),
                SCREEN_HEIGHT - text_surf.get_height(),
            ),
        )
