# Import pygame
import pygame
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
    def __init__(self, filename, position, angle):
        self.angle = angle
        self.image = pygame.image.load(filename)
        self.imageRotated = pygame.transform.rotate(self.image, angle)
        self.position = Position(position[0], position[1])
        self.velocity = Position(0, 0)

    def update(self):
        self.position += self.velocity

    def draw(self):
        self.imageRotated = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.imageRotated, self.position)


class Player(Sprite):
    def update(self):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_RIGHT]:
            self.velocity = Position(10,0)
        elif is_key_pressed[pygame.K_LEFT]:
            self.velocity = Position(-10,0)
        elif is_key_pressed[pygame.K_UP]:
            self.velocity = Position(0, -10)
        elif is_key_pressed[pygame.K_DOWN]:
            self.velocity = Position(0, 10)
        else:
            self.velocity = Position(0,0)
        super().update()


# Initialise pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image

boid1 = Player('gfg.png', (0, 0), 180)
boid2 = Sprite('arrow.png', (300, 300), 180)
boid2.velocity = Position(-1,-1)
# Set the size for the image
DEFAULT_IMAGE_SIZE = (20, 20)

# Rotate the image by any degree


# Set a default position
DEFAULT_IMAGE_POSITION = (20, 20)

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
    clock.tick(30)
    # Maxi was here
