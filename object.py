import pygame
from pygame import Vector2

physicsScale = 3 * 10 ** 8
size = width, height = 1600, 1000


class Object:
    def __init__(self, filename, position, size: tuple[float, float], angle: float, mass: float):
        self.mass: float = mass
        self.angle: float = angle
        self.image = pygame.image.load(filename)
        self.size = Vector2(size[0]/physicsScale, size[1]/physicsScale)
        self.imageScaled = pygame.transform.scale(self.image, self.size)
        self.imageRotated = pygame.transform.rotate(self.imageScaled, angle)
        self.position: Vector2 = Vector2(position[0], position[1])
        self.force: Vector2 = Vector2(0, 0)
        self.velocity: Vector2 = Vector2(0, 0)
        self.acceleration: Vector2 = Vector2(0, 0)
        self.active = False

    def update(self, dt: float):
        if not self.active:
            return
        self.acceleration = self.force * (1.0 / self.mass)
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.force = Vector2(0, 0)

    def setRotation(self, newAngle):
        self.angle = newAngle
        self.imageRotated = pygame.transform.rotate(self.imageScaled, self.angle)

    def draw(self, screen):
        if not self.active:
            return
        screen.blit(self.imageRotated, self.position/physicsScale - self.size * 0.5 + Vector2(width/2, height/2))
