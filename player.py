import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_ACCELERATION,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from shot import Shot


class Player(CircleShape):
    containers = []

    def __init__(self, x, y, lifes):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.lifes = lifes
        self.acceleration = PLAYER_ACCELERATION
        self.acceleration_timeout = 0
        self.weapon_type = "pea_shooter"

    def set_lifes(self, lifes):
        self.lifes = lifes

    def take_life(self):
        self.lifes -= 1
        self.set_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def set_position(self, x, y):
        self.rotation = 0
        self.position = pygame.Vector2(x, y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.weapon_type)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def accelerate(self):
        self.acceleration_timeout = -0.018
        if self.acceleration_timeout < 0:
            self.acceleration += 0.0075

    def move_with_wrap(self, dt, move_forward=True):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        backward = pygame.Vector2(0, -1).rotate(self.rotation)

        if self.position.x > SCREEN_WIDTH:
            self.position = pygame.Vector2(0, self.position.y)
            self.accelerate()
        elif self.position.x < 0:
            self.position = pygame.Vector2(SCREEN_WIDTH, self.position.y)
            self.accelerate()
        elif self.position.y > SCREEN_HEIGHT:
            self.position = pygame.Vector2(self.position.x, 0)
            self.accelerate()
        elif self.position.y < 0:
            self.position = pygame.Vector2(self.position.x, SCREEN_HEIGHT)
            self.accelerate()
        else:
            if move_forward:
                self.position += forward * PLAYER_SPEED * self.acceleration * dt
            else:
                self.position += backward * PLAYER_SPEED * self.acceleration * dt
            self.accelerate()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.weapon_type = "pea_shooter"
        if keys[pygame.K_2]:
            self.weapon_type = "shotgun"
        if keys[pygame.K_3]:
            self.weapon_type = "big_boy"
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move_with_wrap(dt)
        if keys[pygame.K_s]:
            self.move_with_wrap(dt, False)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown > 0:
                pass
            else:
                self.shoot()

        self.shoot_cooldown -= dt
        self.acceleration_timeout += dt

        if self.acceleration_timeout >= 0:
            self.acceleration = PLAYER_ACCELERATION
