import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    def __init__(self):
        self.game_started = False
        self.start_game_rect: pygame.Rect | None = None
        self.restart_game_rect: pygame.Rect | None = None
        self.quit_rect: pygame.Rect | None = None

        self.font = pygame.font.SysFont("Arial", 28)

    def start_game(self):
        self.game_started = True
        self.start_game_rect = None

    def is_start_game_clicked(self, pos):
        if self.start_game_rect == None:
            return False
        
        return self.start_game_rect.collidepoint(pos[0], pos[1])
    
    def is_restart_game_clicked(self, pos):
        if self.restart_game_rect == None:
            return False
        
        return self.restart_game_rect.collidepoint(pos[0], pos[1])
    
    def is_quit_game_clicked(self, pos):
        if self.quit_rect == None:
            return False
        
        return self.quit_rect.collidepoint(pos[0], pos[1])

    def draw_start_game(self, screen):
        start_surf = self.font.render("Start", True, "white")
        self.start_game_rect = screen.blit(
            start_surf,
            (
                SCREEN_WIDTH / 2 - start_surf.get_width(),
                SCREEN_HEIGHT / 2 - start_surf.get_height(),
            ),
        )

        quit_surf = self.font.render("Quit", True, "white")
        self.quit_rect = screen.blit(
            quit_surf,
            (
                SCREEN_WIDTH / 2 - quit_surf.get_width(),
                SCREEN_HEIGHT / 2 - quit_surf.get_height() + 35,
            ),
        )

    def draw_restart_game(self, screen):
        restart_surf = self.font.render("Restart", True, "white")
        self.restart_game_rect = screen.blit(
            restart_surf,
            (
                SCREEN_WIDTH / 2 - restart_surf.get_width(),
                SCREEN_HEIGHT / 2 - restart_surf.get_height(),
            ),
        )

        quit_surf = self.font.render("Quit", True, "white")
        self.quit_rect = screen.blit(
            quit_surf,
            (
                SCREEN_WIDTH / 2 - quit_surf.get_width() - 15,
                SCREEN_HEIGHT / 2 - quit_surf.get_height() + 35,
            ),
        )
