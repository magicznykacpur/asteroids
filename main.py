import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    font = pygame.font.SysFont("Arial", 24)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=((0, 0, 0)))

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split(score)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                if player.lifes <= 0:
                    game_over = True
                    screen.fill(color=((0, 0, 0)))
                    print("Game over!")
                    return
                else:
                    player.take_life()

        for dr in drawable:
            dr.draw(screen)

        text_surf = font.render(
            f"Lives: {player.lives}, Score: {score.score}", True, (255, 255, 255)
        )
        screen.blit(
            text_surf,
            (
                SCREEN_WIDTH - text_surf.get_width(),
                SCREEN_HEIGHT - text_surf.get_height(),
            ),
        )

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
