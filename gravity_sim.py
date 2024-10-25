# Import pygame
import pygame
import math

from pygame import Vector2

from object import Object
from physics import sunMass, earthMass, moonMass, gravityAcceleration

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

sun = Object('Orange_sun_01.png', (width/2, height/2), (100, 100), 0, sunMass)
moon = Object('moon.png', (sun.position.x - 250, height/2), (15, 15), 90, moonMass)
earth = Object('earth.png', (sun.position.x - 300, height/2), (35, 35), 90, earthMass)
moon.velocity = Vector2(0, 200)
earth.velocity = Vector2(0, 130)

earth.active = True
moon.active = True
sun.active = True
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
    a = gravityAcceleration(sun, earth)
    sun.acceleration = a[0]
    earth.acceleration = a[1]
    a = gravityAcceleration(sun, moon)
    sun.acceleration += a[0]
    moon.acceleration += a[1]
    earth.update(dt)
    moon.update(dt)
    sun.update(dt)
    pygame.display.update()

    screen.fill((128, 128, 128))

    earth.draw(screen)
    moon.draw(screen)
    sun.draw(screen)

    # Part of event loop
    clock.tick(60)
    pygame.display.flip()
    # Maxi was here
