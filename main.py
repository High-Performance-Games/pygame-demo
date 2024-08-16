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
# image = pygame.image.load('gfg.png')
boid = pygame.image.load('arrow.png')
# Set the size for the image
DEFAULT_IMAGE_SIZE = (20, 20)

# Rotate the image by any degree
# image = pygame.transform.rotate(image, 180)
boid = pygame.transform.rotate(boid, 180)

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
        angle += 1
    elif is_key_pressed[pygame.K_LEFT]:
        print('left')
        angle -= 1
    screen.fill((128, 128, 128))
    # rota_image = pygame.transform.rotate(image, angle)
    rota_boid = pygame.transform.rotate(boid, angle)
    # screen.blit(rota_image, (0, 0))
    screen.blit(rota_boid, (0, 0))
    pygame.display.update()

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)
    # Maxi was here