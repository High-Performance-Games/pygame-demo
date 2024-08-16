# Import pygame
import pygame
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int
class Sprite:
    def __init__(self, filename, position, angle):
        self.angle = angle
        self.image = pygame.image.load(filename)
        self.imageRotated = pygame.transform.rotate(self.image, angle)
        self.position = position
    def draw(self):
        self.imageRotated = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.imageRotated, self.position)

# Initialise pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image

boid1 = Sprite('gfg.png', (0,0), 180)
boid2 = Sprite('arrow.png', (300,300), 180)
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
    is_key_pressed = pygame.key.get_pressed()

    if is_key_pressed[pygame.K_RIGHT]:
        print('right')
        boid2.angle += 1
    elif is_key_pressed[pygame.K_LEFT]:
        print('left')
        boid2.angle -= 1
    screen.fill((128, 128, 128))

    boid1.draw()
    boid2.draw()
    pygame.display.update()

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
    # Maxi was here