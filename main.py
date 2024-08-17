# Import pygame
import pygame
import time
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int

    def __add__(self, o):
        return Position(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Position(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        return Position(self.x * o.x, self.y * o.y)

    def __truediv__(self, o):
        return Position(self.x / o.x, self.y / o.y)


class Sprite:
    def __init__(self, filename, position, size, angle):
        self.angle = angle
        self.image = pygame.image.load(filename)
        self.imageScaled = pygame.transform.scale(self.image, size)
        self.imageRotated = pygame.transform.rotate(self.imageScaled, angle)
        self.position = Position(position[0], position[1])
        self.velocity = Position(0, 0)

    def update(self):
        self.position += self.velocity
    def setRotation(self, angle):
        self.angle = angle
        self.imageRotated = pygame.transform.rotate(self.imageScaled, self.angle)

    def draw(self):
        screen.blit(self.imageRotated, self.position)

playerSpeed = 5
class Player(Sprite):
    def update(self):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_RIGHT]:
            self.velocity = Position(playerSpeed,0)
        elif is_key_pressed[pygame.K_LEFT]:
            self.velocity = Position(-playerSpeed,0)
        elif is_key_pressed[pygame.K_UP]:
            self.velocity = Position(0, -playerSpeed)
        elif is_key_pressed[pygame.K_DOWN]:
            self.velocity = Position(0, playerSpeed)
        # else:
        #     self.velocity = Position(0,0)
        super().update()


# Initialise pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image

boid1 = Player('playership.png', (300, 300), (50,50),0)
boid2 = Sprite('arrow.png', (300, 300),(50,50), 180)
boid2.velocity = Position(-1,-1)

# Prepare loop condition
running = True
angle = 0
# Event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 128, 128))
    boid1.update()
    boid2.update()

    boid1.draw()
    boid2.draw()
    pygame.display.update()

    # Part of event loop
    pygame.display.flip()
    clock.tick(60)
    # Maxi was here
