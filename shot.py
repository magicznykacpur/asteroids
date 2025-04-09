import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    containers = []

    def __init__(self, x, y, radius, weapon_type="pea_shooter"):
        super().__init__(x, y, radius)
        self.velocity = 0
        self.weapon_type = weapon_type
        self.shotgun_shells: None | tuple = None

    def draw(self, screen):
        if self.weapon_type == "pea_shooter":
            self.draw_pea_shooter(screen)

        if self.weapon_type == "shotgun":
            self.draw_shotgun(screen)

        if self.weapon_type == "big_boy":
            self.draw_big_boy(screen)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw_pea_shooter(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def draw_shotgun(self, screen):
        pygame.draw.circle(screen, "white", self.position.rotate(300 * 0.015), self.radius, 2),
        pygame.draw.circle(screen, "white", self.position, self.radius, 2),
        pygame.draw.circle(screen, "white", self.position.rotate(-300 * 0.015), self.radius, 2),

    def draw_big_boy(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius * 5, 7)
