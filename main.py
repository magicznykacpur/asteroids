import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from menu import Menu
from player import Player
from shot import Shot
from score import Score


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    AsteroidField()

    Player.containers = (updatable, drawable)
    score = Score()
    menu = Menu()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 3)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if menu.is_start_game_clicked(event.pos):
                    menu.start_game()
                    menu.remove_start_game_rect()
                elif menu.is_restart_game_clicked(event.pos):
                    player.set_lifes(3)
                    player.set_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    score.reset_score()
                elif menu.is_quit_game_clicked(event.pos):
                    return
            if event.type == pygame.QUIT:
                return

        screen.fill(color=((0, 0, 0)))

        if not menu.game_started:
            menu.draw_start_game(screen)
        elif menu.game_started and player.lifes <= 0:
            menu.draw_restart_game(screen)
        else:
            updatable.update(dt)

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.detect_collision(shot):
                        asteroid.split(score)

            for asteroid in asteroids:
                if asteroid.detect_collision(player) and player.lifes > 0:
                    player.take_life()

            for dr in drawable:
                dr.draw(screen)

            score.draw(player.lifes, screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
