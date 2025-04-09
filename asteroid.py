import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, score):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            score.update_score(ASTEROID_MIN_RADIUS)
            return
        else:
            random_angle = random.uniform(20, 50)

            new_angle_1 = self.velocity.rotate(random_angle)
            new_angle_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            score.update_score(new_radius)

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = new_angle_1 * 1.2
            new_asteroid_2.velocity = new_angle_2 * 1.2