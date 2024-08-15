# Import pygame
import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('gfg.png')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

# Rotate the image by any degree
image = pygame.transform.rotate(image, 180)

# Set a default position
DEFAULT_IMAGE_POSITION = (200, 200)

# Prepare loop condition
running = True
angle = 0

# Event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    rota_image = pygame.transform.rotate(image, angle)
    screen.blit(rota_image, (0, 0))
    pygame.display.update()
    angle += 1

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
    # Maxi was here