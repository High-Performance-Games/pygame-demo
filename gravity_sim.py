# Import pygame
import pygame
import math

from pygame import Vector2

from object import Object
from physics import earthMass, moonMass, gravityAcceleration

playerSpeed = 15



# Initialise pygame
pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load("test.mp3")
crash_sound = pygame.mixer.Sound("317752__jalastram__sfx_explosion_07.wav")
# pygame.mixer.music.play()

# Set window size
size = width, height = 1600, 1000
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image

earth = Object('earth.png', (width/2, height/2), (100, 100), 0, earthMass)
moon = Object('moon.png', (earth.position.x - 100, height/2), (25, 25), 90, moonMass)
moon2 = Object('moon.png', (earth.position.x - 200, height/2), (25, 25), 90, moonMass)
moon.velocity = Vector2(0, 200)
moon2.velocity = Vector2(0, 130)

earth.active = True
moon.active = True
moon2.active = True
# Prepare loop condition
running = True
angle = 0
gameClock = pygame.time.Clock()
DT_SHIFT = 10
# Event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frameTime = gameClock.tick(60.0)  # attempts to normalize the time between game loops
    dt = frameTime / 1000.0  # divide by ~1000

    a = gravityAcceleration(earth, moon)
    earth.acceleration = a[0]
    moon.acceleration = a[1]
    a = gravityAcceleration(earth, moon2)
    earth.acceleration += a[0]
    moon2.acceleration = a[1]
    a = gravityAcceleration(moon, moon2)
    moon.acceleration += a[0]
    moon2.acceleration += a[1]
    earth.update(dt)
    moon.update(dt)
    moon2.update(dt)
    pygame.display.update()

    screen.fill((128, 128, 128))

    earth.draw(screen)
    moon.draw(screen)
    moon2.draw(screen)

    # Part of event loop
    clock.tick(60)
    pygame.display.flip()
    # Maxi was here
