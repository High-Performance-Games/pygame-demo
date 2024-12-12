# Import pygame
import pygame
import math

from pygame import Vector2

from object import Object


# Initialise pygame
pygame.init()
pygame.mixer.init()

# Set window size
size = width, height = 400, 750
screen = pygame.display.set_mode(size)

playfield = pygame.image.load("pinbotplayfield.png").convert()
shoot_again = pygame.image.load("shoot_again.png").convert()
playfield = pygame.transform.scale(playfield, Vector2(400,750))
shoot_again = pygame.transform.scale(shoot_again, Vector2(400,750))
playfield.blit(shoot_again, (0,0), special_flags=pygame.BLEND_RGB_ADD)
# Using blit to copy content from one surface to other
screen.blit(shoot_again, (0, 0))
# paint screen one time
pygame.display.flip()
status = True
count = 0
lamps = 0
playfieldImg = pygame.image.load("pinbotplayfield.png").convert()
shoot_againImg = pygame.image.load("shoot_again.png").convert()
while (status):

    playfield = pygame.transform.scale(playfieldImg, Vector2(400, 750))
    shoot_again = pygame.transform.scale(shoot_againImg, Vector2(400, 750))
    if(count >> 6):
        lamps = ~lamps
        count = 0
    count += 1
    if(lamps):
        screen.blit(playfield, (0, 0))
    else:
        playfield.blit(shoot_again, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(playfield, (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

    pygame.display.update()
# deactivates the pygame library
pygame.quit()