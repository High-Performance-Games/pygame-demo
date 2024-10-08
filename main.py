# Import pygame
import pygame
import math
from typing import NamedTuple

from pygame import Vector2

from position import Position
from object import Object

playerSpeed = 25


class Player(Object):
    def update(self, dt: float):
        if not self.active:
            return
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_RIGHT]:
            self.velocity = Vector2(playerSpeed, 0)
            self.setRotation(-90)
        elif is_key_pressed[pygame.K_LEFT]:
            self.velocity = Vector2(-playerSpeed, 0)
            self.setRotation(90)
        elif is_key_pressed[pygame.K_UP]:
            self.velocity = Vector2(0, -playerSpeed)
            self.setRotation(0)
        elif is_key_pressed[pygame.K_DOWN]:
            self.velocity = Vector2(0, playerSpeed)
            self.setRotation(180)
        else:
            self.velocity = Vector2(0, 0)

        super().update(dt)


class BoidEnemy(Object):
    def __init__(self, filename, position, size, angle, target):
        super().__init__(filename, position, size, angle)
        self.rotationSpeed = 1
        self.target = target

    def update(self, dt: float):
        if not self.active:
            return
        self.setRotation(self.angle)
        self.rotationSpeed += 0.01
        # self.velocity = Vector2(math.cos(math.pi * self.angle / 180), -math.sin(math.pi * self.angle / 180))
        self.velocity = Vector2((self.target.position.x - self.position.x) * 0.01
                                - math.cos(math.pi * self.angle / 180),
                                (self.target.position.y - self.position.y) * 0.01
                                + math.sin(math.pi * self.angle / 180))
        super().update(dt)


class Projectile(Object):
    def __init__(self, filename, position, size, angle, target):
        super().__init__(filename, position, size, angle)
        self.rotationSpeed = 1
        self.target = target

    def update(self, dt: float):
        if not self.active:
            return
        self.setRotation(self.angle)
        self.rotationSpeed += 0.01
        # self.velocity = Vector2(math.cos(math.pi * self.angle / 180), -math.sin(math.pi * self.angle / 180))
        self.velocity = Vector2((self.target.position.x - self.position.x) * 0.01
                                + math.cos(math.pi * self.angle / 180),
                                (self.target.position.y - self.position.y) * 0.01
                                - math.sin(math.pi * self.angle / 180))
        if self.position.x <= 0:
            pygame.mixer.Sound.play(crash_sound)
            self.active = False
        elif self.position.y <= 0:
            pygame.mixer.Sound.play(crash_sound)
            self.active = False
        elif self.position.x >= 600:
            pygame.mixer.Sound.play(crash_sound)
            self.active = False
        elif self.position.y >= 600:
            pygame.mixer.Sound.play(crash_sound)
            self.active = False

        super().update(dt)


# Initialise pygame
pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load("test.mp3")
crash_sound = pygame.mixer.Sound("317752__jalastram__sfx_explosion_07.wav")
# pygame.mixer.music.play()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image

playerShip = Player('playership.png', (300, 300), (50, 50), 0)
boidEnemy = BoidEnemy('arrow.png', (300, 300), (50, 50), 180, playerShip)
projectile = Projectile('arrow.png', (300, 600), (25, 25), 90, playerShip)

playerShip.active = True
boidEnemy.active = True
projectile.active = True
# Prepare loop condition
running = True
angle = 0
gameClock = pygame.time.Clock()
# Event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frameTime = gameClock.tick(60.0)  # attempts to normalize the time between game loops
    dt = frameTime / 1000.0  # divide by ~1000
    playerShip.update(dt)

    boidEnemy.update(dt)
    projectile.update(dt)
    pygame.display.update()

    screen.fill((128, 128, 128))
    if not projectile.active:
        projectile.active = True
        projectile.position = boidEnemy.position
    playerShip.draw(screen)
    boidEnemy.draw(screen)
    projectile.draw(screen)

    # Part of event loop
    clock.tick(60)
    pygame.display.flip()
    # Maxi was here
