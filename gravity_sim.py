# Import pygame
import pygame
import math

from pygame import Vector2

from object import Object
from object import physicsScale
from physics import sunMass, earthMass, moonMass, gravityAcceleration, sunToEarth, moonToEarth, earthVelocity, \
    gravityForce, earthRadius, moonRadius, sunRadius, moonVelocity, sunToVenus

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

sun = Object('Orange_sun_01.png', (0, 0), (sunRadius * 20, sunRadius * 20), 0, sunMass)
moon = Object('moon.png', (sunToEarth - moonToEarth, 0), (moonRadius * 500, moonRadius * 500), 90, moonMass)
earth = Object('earth.png', (sunToEarth, 0), (earthRadius * 500, earthRadius * 500), 90, earthMass)
venus = Object('earth.png', (sunToVenus, 0), (earthRadius * 500, earthRadius * 500), 90, earthMass)
moon.velocity = Vector2(0, earthVelocity + moonVelocity)
earth.velocity = Vector2(0, earthVelocity)
venus.velocity = Vector2(0, earthVelocity)

earth.active = True
moon.active = True
sun.active = True
venus.active = True
# Prepare loop condition
running = True
angle = 0
gameClock = pygame.time.Clock()
DT_SHIFT = 10
# Event loop
frameTime = gameClock.tick(60.0)  # attempts to normalize the time between game loops

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     print(pos)
        #     earth.position = Vector2((pos[0] - width/2)*physicsScale, (pos[1] - height/2)*physicsScale)
    frameTime = gameClock.tick(60.0)  # attempts to normalize the time between game loops
    dt = frameTime * 10  # divide by ~1000
    for i in range(100):
        gravityForce(moon, earth)
        gravityForce(sun, earth)
        gravityForce(sun, moon)
        gravityForce(sun, venus)
        gravityForce(moon, venus)
        gravityForce(earth, venus)
        earth.update(dt)
        moon.update(dt)
        sun.update(dt)
        venus.update(dt)

    pygame.display.update()

    screen.fill((0, 0, 0))

    earth.draw(screen)
    moon.draw(screen)
    sun.draw(screen)
    venus.draw(screen)

    # Part of event loop
    clock.tick(60)
    pygame.display.flip()
    # Maxi the avali was here
